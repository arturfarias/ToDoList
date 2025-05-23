from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class UserTest(APITestCase):

    def setUp(self):
        self.admin_user = User.objects.create_user(id=1,username='admin', password='adminpass', is_staff=True)
        self.normal_user = User.objects.create_user(id=2, username='user', password='userpass')

    def test_create_user_OK(self):
        response = self.client.post("/user/", {
            'username': 'novoUser',
            'email': 'teste@gmail.com',
            'password': 'Novo@user06',
            'confirm_password': 'Novo@user06'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['username'], 'novoUser')
        self.assertEqual(response.json()['email'], 'teste@gmail.com')

    
    def test_create_user_without_username_BAD_REQUEST(self):
        response = self.client.post("/user/", {
            'email': 'teste@gmail.com',
            'password': 'Novo@user06',
            'confirm_password': 'Novo@user06'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_email_OK(self):
        response = self.client.post("/user/", {
            'username': 'novoUser',
            'password': 'Novo@user06',
            'confirm_password': 'Novo@user06'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['username'], 'novoUser')
        self.assertEqual(response.json()['email'], '')
        

    def test_create_user_without_password_BAD_REQUEST(self):
        response = self.client.post("/user/", {
            'username': 'novoUser',
            'email': 'teste@gmail.com',
            'confirm_password': 'Novo@user06'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_confirm_password_BAD_REQUEST(self):
        response = self.client.post("/user/", {
            'username': 'novoUser',
            'email': 'teste@gmail.com',
            'password': 'Novo@user06',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_different_password_BAD_REQUEST(self):
        response = self.client.post("/user/", {
            'username': 'novoUser',
            'email': 'teste@gmail.com',
            'password': 'Novo@user06',
            'confirm_password': '1234567'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_users_with_auth(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get("/user/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()[0]['username'], 'admin')
        self.assertEqual(response.json()[1]['username'], 'user')


    def test_get_users_requires_auth(self):
        response = self.client.get("/user/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_by_id_users_with_auth_get_self(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(f"/user/{self.normal_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'user')

    def test_get_by_id_users_with_auth_get_other(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get(f"/user/{self.admin_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_by_id_admin_with_auth_get_self(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(f"/user/{self.admin_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'admin')

    def test_get_by_id_admin_with_auth_get_other(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(f"/user/{self.normal_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_requires_auth(self):
        response = self.client.get(f"/user/{self.normal_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_users_with_auth_get_self(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.put(f"/user/{self.normal_user.id}/", {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_users_with_auth_get_other(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.put(f"/user/{self.admin_user.id}/", {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        })
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_admin_with_auth_get_self(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(f"/user/{self.admin_user.id}/", {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_admin_with_auth_get_other(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(f"/user/{self.normal_user.id}/", {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_requires_auth(self):
        response = self.client.put(f"/user/{self.normal_user.id}/", {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        }) 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_delete_users_with_auth_get_self(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(f"/user/{self.normal_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_users_with_auth_get_other(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.delete(f"/user/{self.admin_user.id}/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_admin_with_auth_get_self(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f"/user/{self.admin_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_admin_with_auth_get_other(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f"/user/{self.normal_user.id}/")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_requires_auth(self):
        response = self.client.delete(f"/user/{self.normal_user.id}/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_OK(self):
        response = self.client.post("/api/token/", {
            'username': 'admin',
            'password': 'adminpass',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)