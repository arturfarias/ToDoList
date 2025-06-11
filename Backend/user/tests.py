import copy

from rest_framework.test import APITestCase
from rest_framework import status

from utils.seeds import DataSeeder


class UserTest(APITestCase):

    def setUp(self):
        self.admin_user, self.normal_user = DataSeeder().get_users('admin', 'user')

        base_user = {
            'username': 'novoUser',
            'email': 'teste@gmail.com',
            'password': 'Novo@user06',
            'confirm_password': 'Novo@user06'
        }

        self.valid_user = base_user.copy()

        self.missing_username_user = base_user.copy()
        self.missing_username_user.pop('username')

        self.missing_email_user = base_user.copy()
        self.missing_email_user.pop('email')

        self.missing_password_user = base_user.copy()
        self.missing_password_user.pop('password')

        self.missing_confirm_password_user = base_user.copy()
        self.missing_confirm_password_user.pop('confirm_password')

        self.different_password_user = base_user.copy()
        self.different_password_user['confirm_password'] = '1234567'
        
        self.updated_user = {
            'username': 'update',
            'email': 'update@gmail.com',
            'password': 'update',
            'confirm_password': 'update'
        }
        
        self.login = {
            'username': 'admin',
            'password': 'adminpass',
        }
    

    def test_create_user_OK(self):
        response = self.client.post("/user/", self.valid_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['username'], 'novoUser')
        self.assertEqual(response.json()['email'], 'teste@gmail.com')

    
    def test_create_user_without_username_BAD_REQUEST(self):
        response = self.client.post("/user/", self.missing_username_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_email_OK(self):
        response = self.client.post("/user/", self.missing_email_user)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        self.assertEqual(response.json()['username'], 'novoUser')
        self.assertEqual(response.json()['email'], '')
        

    def test_create_user_without_password_BAD_REQUEST(self):
        response = self.client.post("/user/", self.missing_password_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_confirm_password_BAD_REQUEST(self):
        response = self.client.post("/user/", self.missing_confirm_password_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_different_password_BAD_REQUEST(self):
        response = self.client.post("/user/", self.different_password_user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_users_with_auth(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.get("/user/")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json()['results'][0]['username'], 'admin')
        self.assertEqual(response.json()['results'][1]['username'], 'user')


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
        response = self.client.put(f"/user/{self.normal_user.id}/", self.updated_user)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_users_with_auth_get_other(self):
        self.client.force_authenticate(user=self.normal_user)
        response = self.client.put(f"/user/{self.admin_user.id}/", self.updated_user)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_admin_with_auth_get_self(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(f"/user/{self.admin_user.id}/", self.updated_user)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_admin_with_auth_get_other(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.put(f"/user/{self.normal_user.id}/", self.updated_user)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'update')
        self.assertEqual(response.json()['email'], 'update@gmail.com')

    def test_update_requires_auth(self):
        response = self.client.put(f"/user/{self.normal_user.id}/", self.updated_user) 
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
        response = self.client.post("/api/token/", self.login)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_me_as_admin_OK(self):
        self.client.force_authenticate(user=self.admin_user)

        response = self.client.get("/user/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'admin')

    def test_me_as_user_OK(self):
        self.client.force_authenticate(user=self.normal_user)

        response = self.client.get("/user/me/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()['username'], 'user')