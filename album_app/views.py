from django.shortcuts import render
from . models import album_db,album_db2
# Create your views here.
def index(request):
    album_loop = album_db.objects.all()
    context = {'album_loop' : album_loop}
    return render(request,'album_app/index.html',context)
def next(request):
    album_loop2 = album_db2.objects.all()
    context = {'album_loop2' : album_loop2}
    return render(request,'album_app/next.html',context)