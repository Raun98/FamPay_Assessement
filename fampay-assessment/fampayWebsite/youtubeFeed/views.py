#Django Packages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.template import loader
from django.http import HttpResponse

#Background_Tasks Packages
from background_task.models import Task

#Other
from .models import Video_Info
from .tasks import create_data

# Create your views here.
def index(request):
    preprocessing(repeat=100)                                 #Purge Database
    vids = Video_Info.objects.all().order_by('-published_at') #Descending Order of results
    pag = Paginator(vids, 5)                                  #Pagination
    page = request.GET.get('page')                            #GET api
    videos_per_page = pag.get_page(page)
    template=loader.get_template('youtubeFeed/feed.html')
    return HttpResponse(template.render({'Videos': videos_per_page},request))

def preprocessing(repeat):
    Task.objects.all().delete()
    create_data(repeat=repeat)

