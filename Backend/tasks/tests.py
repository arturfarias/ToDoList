import copy

from rest_framework.test import APITestCase
from rest_framework import status
from datetime import timezone, timedelta, datetime


from utils.seeds import DataSeeder

class UserTest(APITestCase):

    def setUp(self):
        self.user, self.admin = DataSeeder().get_users('user', 'admin')

        tz = timezone(timedelta(hours=-3))
        self.date_time = datetime.now()
        self.date_time = self.date_time.replace(tzinfo=tz)

        base_task = {
            'owner': self.user.id,
            'title': 'Test',
            'description': 'Is a Test',
            'tags': [],
            'topics': []
        }

        self.valid_task = base_task.copy()
        
        self.valid_task_whit_tag = copy.deepcopy(base_task)
        self.valid_task_whit_tag['tags'].append(1)

        self.valid_task_whit_topic = copy.deepcopy(self.valid_task_whit_tag)
        self.valid_task_whit_topic['topics'].append({'description': 'topic description'})
        
        self.missing_owner_task = base_task.copy()
        self.missing_owner_task.pop('owner')

        self.missing_title_task = base_task.copy()
        self.missing_title_task.pop('title')

        self.missing_description_task = base_task.copy()
        self.missing_description_task.pop('description')

        self.missing_tags_task = base_task.copy()
        self.missing_tags_task.pop('tags')

        self.missing_topics_task = base_task.copy()
        self.missing_topics_task.pop('topics')

        
        self.updated_task = {
            "owner": self.admin.id,
            "title": "update",
            "description": "update",
            "tags": [1,2],
            "topics": [
                {
                    "description": "update 1",
                    "is_done": True,
                    "finished_at": self.date_time,
                },
                {
                    "description": "update 2",
                    "is_done": True,
                    "finished_at": self.date_time,
                },
            ],
        }

        self.updated_task_more_tags = copy.deepcopy(self.updated_task)
        self.updated_task_more_tags['tags'].append(3)

        self.updated_task_less_tags = copy.deepcopy(self.updated_task)
        self.updated_task_less_tags['tags'].pop()

        self.updated_task_bad_request = copy.deepcopy(self.updated_task)
        self.updated_task_bad_request['tags'].append(99999)

        self.updated_task_more_topics = copy.deepcopy(self.updated_task)
        self.updated_task_more_topics['topics'].append({
                                                        "description": "update 3",
                                                        "is_done": False,
                                                    },)

        self.updated_task_less_topics = copy.deepcopy(self.updated_task)
        self.updated_task_less_topics['topics'].pop()


    def test_get_tasks_requires_auth(self):
        response = self.client.get("/task/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tasks(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/task/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json()['results'][0]['title'], 'test')
        self.assertEqual(response.json()['results'][1]['title'], 'test2')

    def test_create_task_OK(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.valid_task, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['owner'], self.user.id)
        self.assertEqual(response.json()['title'], 'Test')
        self.assertEqual(response.json()['description'], 'Is a Test')
        self.assertEqual(response.json()['tags'], [])
        self.assertEqual(response.json()['topics'], [])

    def test_create_task_with_tag_OK(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.valid_task_whit_tag, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['owner'], self.user.id)
        self.assertEqual(response.json()['title'], 'Test')
        self.assertEqual(response.json()['description'], 'Is a Test')
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(response.json()['topics'], [])

    def test_create_task_with_topic_OK(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.valid_task_whit_topic, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['owner'], self.user.id)
        self.assertEqual(response.json()['title'], 'Test')
        self.assertEqual(response.json()['description'], 'Is a Test')
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(response.json()['topics'][0]['description'], 'topic description')

    def test_create_task_without_owner_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.missing_owner_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_without_title_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.missing_title_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_without_description_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.missing_description_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_without_tags_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.missing_tags_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_without_topics_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/task/", self.missing_topics_task)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_requires_auth(self):
        response = self.client.get("/task/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_by_id_task_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/task/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['owner'], self.user.id)
        self.assertEqual(response.json()['title'], 'test')
        self.assertEqual(response.json()['description'], 'is a test')
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(response.json()['tags'][1]['name'], 'black')
        self.assertEqual(response.json()['tags'][1]['color'], '#000000')
        self.assertEqual(response.json()['topics'][0]['description'], 'test task 1')
        self.assertEqual(response.json()['topics'][0]['is_done'], False)
        self.assertEqual(response.json()['topics'][1]['description'], 'test task 2')
        self.assertEqual(response.json()['topics'][1]['is_done'], False)

    def test_get_by_id_task_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/task/9999/")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_by_id_requires_auth(self):
        response = self.client.get("/task/1/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_task_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['owner'], self.admin.id)
        self.assertEqual(response.json()['title'], 'update')
        self.assertEqual(response.json()['description'], 'update')
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(response.json()['tags'][1]['name'], 'black')
        self.assertEqual(response.json()['tags'][1]['color'], '#000000')
        self.assertEqual(response.json()['topics'][0]['description'], 'update 1')
        self.assertEqual(response.json()['topics'][0]['is_done'], True)
        self.assertEqual(response.json()['topics'][0]['finished_at'], self.date_time.isoformat())
        self.assertEqual(response.json()['topics'][1]['description'], 'update 2')
        self.assertEqual(response.json()['topics'][1]['is_done'], True)
        self.assertEqual(response.json()['topics'][1]['finished_at'], self.date_time.isoformat())       

    def test_update_requires_auth(self):
        response = self.client.put("/task/1/", self.updated_task) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_update_task_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/9999/", self.updated_task)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_update_task_with_auth_add_tags(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task_more_tags, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(response.json()['tags'][1]['name'], 'black')
        self.assertEqual(response.json()['tags'][1]['color'], '#000000')
        self.assertEqual(response.json()['tags'][2]['name'], 'yellow')
        self.assertEqual(response.json()['tags'][2]['color'], '#ffde21')
        self.assertEqual(len(response.json()['tags']), 3)

    def test_update_task_with_auth_remove_tags(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task_less_tags, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['tags'][0]['name'], 'red')
        self.assertEqual(response.json()['tags'][0]['color'], '#FF0000')
        self.assertEqual(len(response.json()['tags']), 1)

    def test_update_task_with_auth_add_tags_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task_bad_request, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_task_with_auth_add_topics(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task_more_topics, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['topics'][0]['description'], 'update 1')
        self.assertEqual(response.json()['topics'][0]['is_done'], True)
        self.assertEqual(response.json()['topics'][0]['finished_at'], self.date_time.isoformat())
        self.assertEqual(response.json()['topics'][1]['description'], 'update 2')
        self.assertEqual(response.json()['topics'][1]['is_done'], True)
        self.assertEqual(response.json()['topics'][1]['finished_at'], self.date_time.isoformat())
        self.assertEqual(response.json()['topics'][2]['description'], 'update 3')
        self.assertEqual(response.json()['topics'][2]['is_done'], False)
        self.assertEqual(response.json()['topics'][2]['finished_at'], None)
        self.assertEqual(len(response.json()['topics']), 3)

    def test_update_task_with_auth_remove_topics(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/task/1/", self.updated_task_less_topics, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['topics'][0]['description'], 'update 1')
        self.assertEqual(response.json()['topics'][0]['is_done'], True)
        self.assertEqual(response.json()['topics'][0]['finished_at'], self.date_time.isoformat())
        self.assertEqual(len(response.json()['topics']), 1)


    def test_delete_task_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/task/1/")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_task_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/task/9999/")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_requires_auth(self):
        response = self.client.delete("/task/1/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
