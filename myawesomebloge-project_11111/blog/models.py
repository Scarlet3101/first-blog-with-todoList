from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 300)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    image = models.FileField(upload_to ='event_images/')

    def get_summary(self):
        return self.text[:200] + "..."

#       "это чтобы в админке были название постов"
    def __str__(self):
        return self.title
