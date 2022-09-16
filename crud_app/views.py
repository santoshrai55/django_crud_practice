from audioop import reverse
from django.shortcuts import render, redirect
from . models import Blog
from . forms import BlogForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    context = Blog.objects.all()
    contents = {'context': context}
    return render(request, 'crud_app/home.html', contents)


def home_detail(request, title):
    blog = Blog.objects.get(title=title)

    return render(request, 'crud_app/blog_detail.html', {'blog': blog})


@login_required
def blog_create(request):
    context = Blog.objects.all()

    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            return render(request, 'crud_app/home.html', {'context': context})
    else:
        return render(request, 'crud_app/blog_create.html', {'form': form})


@login_required
def profile(request):
    current_user = request.user
    return render(request, 'crud_app/profile.html', {'current_user': current_user})


@login_required
def edit_post(request, title):
    blog = Blog.objects.get(title=title)
    if request.method == 'POST':
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_app:blog_detail', title=title)
    else:
        form = BlogForm(instance=blog)
        return render(request, 'crud_app/edit.html', {'form': form})
