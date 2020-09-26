'''Fampay Backend dev project'''

import os
from datetime import datetime, timedelta
#Google's API client
from apiclient.discovery import build
import apiclient

#Background Tasks
from background_task import background
from background_task.models import Task


from .models import *
from fampayWebsite import settings



@background(schedule=10)
def create_data():
    #repeat=repeat
    
    apiKeys = settings.GOOGLE_API_KEYS
    print("Background task running...")

    faultLess = False
    objs=Video_Info.objects.all()
    existing=set()
    for i in objs.iterator():
        existing.add(i.vid_id)
    fetched=set()
    for random_iterator in range(5):
        for apiKey in apiKeys:
            try:
                youtube = build("youtube", "v3", developerKey=apiKey)
                req = youtube.search().list(q="football", part="snippet", order="date", maxResults=50,
                                            publishedAfter=((datetime.now() - timedelta(minutes=10)).replace(microsecond=0).isoformat()+'Z'))
                res = req.execute()
                faultLess = True
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                if not(code == 400 or code == 403):
                    break

            if not(faultLess==False):
                break
        if faultLess:
            print('populating databases...')                     #storing items into the database
            for item in res['items']:
                if item['id']['videoId'] not in existing:
                    video_id = item['id']['videoId']
                    publishedDateTime = item['snippet']['publishedAt']
                    title = item['snippet']['title']
                    description = item['snippet']['description']
                    thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
                    fetched.add(video_id)
                    stored=Video_Info(
                        vid_id=video_id,
                        title=title,
                        description=description,
                        published_at=publishedDateTime,
                        thumbnail_url=thumbnailsUrls,
                    )
                    stored.save()                    #Comminting the changes
                else:
                    continue                         #debugging
        print('finished executing background tasks')