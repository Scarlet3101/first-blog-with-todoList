from django.db import models
# Create your models here.

class Event(models.Model):
    topic = models.CharField(max_length = 20,blank=True)
    event_image = models.ImageField(upload_to ='event_images/',height_field=None, width_field=None,)
    event_text = models.CharField(max_length = 300)
    date_of_post = models.DateField(null=True)
    text = models.TextField(blank=True)

    def get_summary(self):
        return self.text[:135] + "..."

#       "это чтобы в админке были название постов"
    def __str__(self):
        return self.event_text
