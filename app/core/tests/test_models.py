from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        #Test new user with email or something
        email = 'test@email.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        #Test user with weird email
        email = 'test@EMAIL.com'
        user = get_user_model().objects.create_user(
            email = email,
            password='12345'
        )

        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        #Test user with email that aint an email
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(
                email = None,
                password='12345'
            )

    def test_create_new_superuser(self):
        #Create a superuser
        user = get_user_model().objects.create_superuser(
            email='test@email.com',
            password='12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
