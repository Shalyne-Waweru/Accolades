from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
  '''
  Test class that defines test cases for the model behaviours.

  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''

  def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''
      #Create and save a User
      self.user = User.objects.create(username='sha')

      self.new_profile = Profile(user=self.user, profile_pic='media/profile-images/img1.jpg', bio='This is my bio') 

  # FIRST TEST
  def test_instance(self):
      '''
      test_instance test case to test if the object is initialized properly
      '''
      self.assertTrue(isinstance(self.new_profile,Profile))

  # SECOND TEST
  def test_save_profile(self):
      '''
      test_save_profile test case to test if the object is being saved correctly
      '''
      self.new_profile.save_profile()
      self.assertTrue(len(Profile.objects.all()) > 0)

  # THIRD TEST
  def test_update_profile(self):
      '''
      test_update_profile test case to test if the object is being updated correctly
      '''
      self.new_profile.save_profile()
      self.new_profile.bio = 'This is my new bio'
      self.assertTrue(self.new_profile.bio  == 'This is my new bio' )

  # FOURTH TEST
  def test_delete_profile(self):
      '''
      test_delete_profile test case to test if the object is being deleted correctly
      '''
      self.new_profile.save_profile()
      self.new_profile.del_profile()
      self.assertTrue(len(Profile.objects.all()) == 0)