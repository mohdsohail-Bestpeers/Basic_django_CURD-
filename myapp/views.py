from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

from django.contrib.auth.forms import UserCreationForm


def BlogView(request):
    obj = Blog.objects.all()
    
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        form.save()
    return render(request,'index.html', {'obj':obj,'form':form})


def UpdateBlog(request,pk):
    obj= Blog.objects.get(id=pk)
    form = BlogForm(instance=obj)
    if request.method=='POST':
        form = BlogForm(request.POST, instance=obj)
        form.save()
        return redirect('BlogView')
    return render(request,'update.html',{'obj':obj,'form':form})

def DeleteBlog(request,pk):
    obj = Blog.objects.get(id=pk)
    obj.delete()
    return redirect('BlogView')

