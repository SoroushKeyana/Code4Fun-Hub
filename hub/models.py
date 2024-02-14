from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project_file = models.FileField(upload_to='')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def searchable_content(self):
        return f"{self.title} {self.description} {self.created_by.username}"
  
    def __str__(self):
        return self.title
    

class ForumCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ForumPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(ForumCategory, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forum_posts_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def searchable_content(self):
        return f"{self.title} {self.content} {self.created_by.username}"

    def __str__(self):
        return self.title

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    