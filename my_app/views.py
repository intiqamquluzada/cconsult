from django.shortcuts import redirect, render
from my_app.models import (Blog, Service, Comment, AboutModel, AboutSideBar,
                           SosialMedia, Subscribe, HomeSlider, Quota, Testimonial, Team,
                           MainDetails)
from my_app.forms import ContactForm, QuotaForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index_view(request):


    if request.method == "POST":
        sub_email = request.POST.get("sub")
        if sub_email:
            obj = Subscribe.objects.create(
                email=sub_email
            )
            obj.save()

    sliders = HomeSlider.objects.all()

    context = {
        'sliders': sliders,

    }

    return render(request, 'index.html', context)


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

    blog = request.GET.get('blog')  # search
    if blog is not None:
        blogs = blogs.filter(title__icontains=blog)

    paginator = Paginator(blogs, 1)  # pagination
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'p': p
    }
    return render(request, 'blog.html', context)


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog)  # comment

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


def about_view(request):
    about = AboutModel.objects.first()
    side_bar = AboutSideBar.objects.first()
    socials = SosialMedia.objects.all()
    context = {
        'about': about,
        'side_bar': side_bar,
        'socials': socials
    }
    return render(request, 'about.html', context)


def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


def quote_view(request):
    form = QuotaForm()

    if request.method == 'POST':
        form = QuotaForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = QuotaForm()

    quote = Quota.objects.all()
    context = {
        'quote': quote,
        'form': form
    }
    return render(request, 'quote.html', context)


def testimonial_view(request):
    reyler = Testimonial.objects.all()

    context = {
        'reyler': reyler

    }
    return render(request, 'testimonial.html', context)


def team_view(request):
    comanda = Team.objects.all()

    context = {
        'comanda': comanda

    }
    return render(request, 'team.html', context)
