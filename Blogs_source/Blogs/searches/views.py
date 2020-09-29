from django.shortcuts import render
from .models import SearchModel
from my_app.models import BlogPost


# Create your views here.


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    obj = 0
    if request.user.is_authenticated:
        user = request.user
    context = {"query_data": query}
    if query is not None:
        obj = SearchModel.objects.create(query=query, user=user)
        blog_list = BlogPost.objects.search(query=query)
        context["blog_list"] = blog_list
        context["object_data"] = obj

    template_name = "searches/results.html"
    return render(request, template_name, context)
