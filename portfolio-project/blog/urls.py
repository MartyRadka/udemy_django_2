from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>', views.detail, name='detail'),
    # this is an url path to each blog post via ID
    # when someone goes to the blog/1 - it's an int so I save it like a blog_id
    # and I will call the view.detail and in views.py I pass a request and the ID
    # and with this ID I go to the database and take every infos about this ID
    # and sent it to the detail.html from where it's displayed to users
]
