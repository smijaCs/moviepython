from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import updates
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = updates.objects.all()
    return  render(request,"index.html",{'result':movie})
def details(request,movie_id):
    home= updates.objects.get(id=movie_id)
    return render(request,"details.html",{'page':home})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img=request.FILES['img']
        movie=updates(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")

def movie_update(request,id):
     movie=updates.objects.get(id=id)
     form=MovieForm(request.POST or None,request.FILES,instance=movie)
     if form.is_valid():
         form.save()
         return redirect('/')
     return render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
     if request.method=='POST':
        movie=updates.objects.get(id=id)
        movie.delete()
        return  redirect('/')
     return render(request,"delete.html")










