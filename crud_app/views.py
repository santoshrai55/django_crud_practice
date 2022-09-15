from audioop import reverse
from django.shortcuts import render, redirect
from . models import Blog
from . forms import BlogForm
# Create your views here.


def home(request):
    context = Blog.objects.all()
    contents = {'context': context}
    return render(request, 'crud_app/home.html', contents)


def home_detail(request, title):
    blog = Blog.objects.get(title=title)

    return render(request, 'crud_app/blog_detail.html', {'blog': blog})


def blog_create(request):
    form = BlogForm
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('crud_app:home'))
    return render(request, 'crud_app/blog_create.html', {'form': form})
