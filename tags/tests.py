import copy

from rest_framework.test import APITestCase
from rest_framework import status

from utils.seeds import DataSeeder

class UserTest(APITestCase):

    def setUp(self):
        self.user, self.admin = DataSeeder().get_users('user', 'admin')

        base_tag = {
            'name': 'blue',
            'color': '#0000FF',
        }

        self.valid_tag = base_tag.copy()

        self.missing_name_tag = base_tag.copy()
        self.missing_name_tag.pop('name')

        self.missing_color_tag = base_tag.copy()
        self.missing_color_tag.pop('color')

        self.much_characters_color_tag = base_tag.copy()
        self.much_characters_color_tag['color'] = '#00000000'

        self.updated_tag = {
            'name': 'yellow',
            'color': '#FFFF00',
        }



    def test_get_tasks_requires_auth(self):
        response = self.client.get("/tag/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tags(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/tag/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json()['results'][0]['name'], 'red')
        self.assertEqual(response.json()['results'][1]['name'], 'black')

    def test_create_tag_OK(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/tag/", self.valid_tag)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['name'], 'blue')
        self.assertEqual(response.json()['color'], '#0000FF')

    def test_create_tag_without_name_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/tag/", self.missing_name_tag)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_tag_without_color_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/tag/", self.missing_color_tag)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_tag_much_characters_color_BAD_REQUEST(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/tag/", self.much_characters_color_tag)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_tag_requires_auth(self):
        response = self.client.get("/tag/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_get_by_id_tag_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/tag/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['name'], 'red')
        self.assertEqual(response.json()['color'], '#FF0000')

    def test_get_by_id_tag_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get("/tag/9999/")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_by_id_requires_auth(self):
        response = self.client.get("/tag/1/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_tag_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/tag/1/", self.updated_tag)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['name'], 'yellow')
        self.assertEqual(response.json()['color'], '#FFFF00')

    def test_update_tag_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put("/tag/9999/", self.updated_tag)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_requires_auth(self):
        response = self.client.put("/tag/1/", self.updated_tag) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tag_with_auth(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/tag/1/")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_tag_with_auth_NOT_FOUND(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete("/tag/9999/")
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_requires_auth(self):
        response = self.client.delete("/tag/1/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)