from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})


def detail(request, blog_id):
    """The function get_object_or_404 takes the object and it's pk. If there
    is no object it displays the 404 error page"""
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blogdetail})
