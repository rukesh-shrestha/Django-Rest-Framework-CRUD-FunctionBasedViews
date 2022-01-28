from rest_framework.test import APITestCase
from .models import User

# Create your tests here.
class TestModels(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="admin", email="admin@gmail.com")
        self.assertIsInstance(user,User)
        self.assertEqual(user.username,"admin")
        self.assertEqual(user.email,"admin@gmail.com")
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        
    def test_create_super_user(self):
        user = User.objects.create_superuser(username="admin", email="admin@gmail.com")
        self.assertIsInstance(user,User)
        self.assertEqual(user.username,"admin")
        self.assertEqual(user.email,"admin@gmail.com")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    def test_create_user_without_username(self):       
        self.assertRaises(ValueError,User.objects.create_user,username="",email="admin@gmail.com")
   
    def test_create_user_without_email(self):       
        self.assertRaises(ValueError,User.objects.create_user,username="admin",email="")
        
        
    def test_create_super_user_is_staff(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username="rukesh", email="rukesh@gmail.com",is_staff=False)
        
    def test_create_super_user_is_superuser(self):
        self.assertRaises(ValueError,User.objects.create_superuser,username="rukesh", email="rukesh@gmail.com",is_superuser=False)
   