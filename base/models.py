from django.db import models

# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length=200)
  email = models.EmailField(unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
    
class Question(models.Model):
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  content = models.TextField()
  is_correct = models.BooleanField()


class Main(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)


class Room(models.Model):
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return self.name
