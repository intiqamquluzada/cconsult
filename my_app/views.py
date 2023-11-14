from django.shortcuts import redirect, render
from my_app.models import Blog, Service, Comment
from django.contrib.auth import authenticate, login, logout


def service_view(request):
    obj = Service.objects.all()

    context = {
        'obj': obj,
    }
    return render(request, 'service.html', context)


def detail_view(request, slug):
    obj1 = Service.objects.get(slug=slug)

    context = {
        'obj1': obj1
    }
    return render(request, 'service-detail.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('service')

    context = {}

    return render(request, "login.html", context)


def logout_view(request):
    logout(request)
    return redirect("service")


def blog_view(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, 'blog.html', context)


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        comment = request.POST.get("comment")
        my_obj = Comment.objects.create(
            text=comment, user=request.user, blog=blog
        )
        my_obj.save()

    context = {
        'blog': blog,
        "comments": comments

    }
    return render(request, 'detail.html', context)

# class Animal:
#     age = ...
#     name = ...
#     color = ...
#
# obj_1 = Animal(age=7, name='Mestan', color='gray')