from contextlib import redirect_stderr
from django.conf import settings
from django.urls import path, re_path
from . import views

app_name = "my_app"

urlpatterns = [
    path("blog/", views.blog_post_list_view, name="blog_post_list_page"),
    path("blog/<str:my_slug>/", views.blog_post_detail_view, name="blog_post_detail_page"),
    path("blog/<str:my_slug>/update/    ", views.blog_post_update_view, name="blog_post_update_page"),
    path("blog/<str:my_slug>/delete/", views.blog_post_delete_view, name="blog_post_delete_page"),
    path("blog-new/", views.blog_post_create_view, name="blog_post_create_page"),


/

# common pages
    path("home/", views.home_page_view, name="home_page"),
    path("contact/", views.contact_page_view, name="contact_page"),
    path("about/", views.about_page_view, name="about_page"),
    # path("blog/<str:my_slug>/", views.blog_detail_view, name="blog_detail_page"),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
