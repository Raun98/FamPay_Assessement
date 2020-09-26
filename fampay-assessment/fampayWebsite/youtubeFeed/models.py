from django.db import models

#Video Info : To store the video information retrieved from the Youtube Data v3 API
#Fields : Video ID, Title, Description, Published At, Thumbnail URL
class Video_Info(models.Model):
    vid_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True, db_index=True)
    thumbnail_url = models.CharField(max_length=500)

    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),        #Meta Class to create database index
        ]

