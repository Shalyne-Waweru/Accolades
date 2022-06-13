from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  profile_pic = models.ImageField(upload_to='profile-images/', default='default.png')
  bio = models.TextField(max_length=500, default="My Bio", blank=True)

  def __str__(self):
        return f'{self.user.username} Profile Details'

  #Create a profile for every signed in user
  @receiver(post_save, sender=User)
  def update_user_profile(sender, instance, created, **kwargs):
      if created:
          Profile.objects.create(user=instance)
      instance.profile.save()

  def save_profile(self):
    self.save()

  def del_profile(self):
    self.delete()

class Project(models.Model):
  #Create a foreign key column that will store the ID of the User from the User table
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='projects')
  title = models.CharField(max_length=250)
  image = models.ImageField(upload_to = 'project-images/')
  description = models.TextField()
  link = models.CharField(max_length=250)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.title

  def save_project(self):
    self.save()

  def del_project(self):
    self.delete()

  @classmethod
  def search_project(cls, search_term):
    #The __icontains query filter will check if any word in the title field of our project matches the search_term
    projects = cls.objects.filter(user__projects__title__icontains=search_term)
    return projects

  @classmethod
  def get_project_by_id(cls, id):
    project = cls.objects.filter(id = id).first()
    return project