from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_list_view(request):
    now = timezone.now()
    # qs = BlogPost.objects.all().published()
    qs = BlogPost.objects.published()
    # qs = BlogPost.objects.filter(publish_date__lte=now)
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = "my_app/blog_post_list.html"
    context = {"object_list": qs
               }
    return render(request, template_name, context)


@staff_member_required()
# @login_required
def blog_post_create_view(request):
    print(request.POST)
    print(request.user)
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        """if form.is_valid():
        form.save()"""
        """obj = form.save(commit=False)
        obj.title = form.cleaned_data.get('title')
        obj.save()"""
        form = BlogPostModelForm()
    template_name = "my_app/forms.html"
    context = {"my_form": form
               }
    return render(request, template_name, context)


""" form = BlogPostForm(request.POST or None)
    if form.is_valid():
        obj = BlogPost.objects.create(**form.cleaned_data)
        form = BlogPostForm()
    template_name = "my_app/forms.html"
    context = {"my_form": form
               }
"""


@staff_member_required()
def blog_post_detail_view(request, my_slug):
    obj = get_object_or_404(BlogPost, slug=my_slug)

    template_name = "my_app/blog_post_detail.html"
    context = {"detail_obj": obj}
    return render(request, template_name, context)


@staff_member_required()
def blog_post_update_view(request, my_slug):
    data = get_object_or_404(BlogPost, slug=my_slug)
    form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
    template_name = "my_app/forms.html"
    context = {"object_update": data,
               "my_form": form,
               "my_title": f'Update {data.title}'}
    return render(request, template_name, context)


@staff_member_required()
def blog_post_delete_view(request, my_slug):
    obj = get_object_or_404(BlogPost, slug=my_slug)
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    template_name = "my_app/blog_post_delete.html"
    context = {"obj_delete": obj,
               }
    return render(request, template_name, context)


# -------------------------------------------------------------- #


def home_page_view(request):
    title = "Welcome to Home Page"
    qs = BlogPost.objects.all().published()
    # return HttpResponse("<h1> Hello World </h1>")
    context = {"home_object": qs,
               "title": title,
               }
    return render(request, "my_app/home.html", context)


def about_page_view(request):
    my_title = "about "
    context = {"obj": my_title
               }
    # return HttpResponse("<h1> About page </h1>")
    return render(request, "my_app/about.html", context)


def contact_page_view(request):
    my_title = "Contact"
    context = {"obj": my_title
               }
    # return HttpResponse("<h1> Contact page </h1>")
    return render(request, "my_app/contact.html", context)


def blog_detail_view(request, my_slug):
    # queryset = BlogPost.objects.filter(slug=my_slug)
    # obj = BlogPost.objects.get(id=my_id)
    obj = get_object_or_404(BlogPost, slug=my_slug)

    template_name = "my_app/blog_detail.html"
    context = {
        "obj": obj
    }
    return render(request, template_name, context)
