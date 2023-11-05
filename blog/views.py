from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from blog.models import Blog,Category

from .models import Blog, Category


# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True,is_active=True),
        "categories": Category.objects.all()
    }
    return render(request,"blog/index.html",context)

def blog(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request,"blog/blogs.html",context)

def blog_details(request,slug):
    # blogs = data["blogs"]
    # selectedBlog=None

    # for blog in blogs:
    #     if blog["id"]==id:
    #         selectedBlog = blog
    # blogs = data["blogs"]

    # selectedBlog=[blog for blog in blogs if blog["id"]==id][0]
    blog=Blog.objects.get(slug=slug)
    return render(request,"blog/blog-details.html", {
        "blog":blog
    })


def blogs_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)

  
    blogs = Blog.objects.filter(is_active=True, category=category)
    categories = Category.objects.all()
    context = {
        "blogs": blogs,
        "categories": categories,
        "selected_category": category,  
    }
    return render(request, "blog/blogs.html", context)