from django.urls import path
from . import views
urlpatterns=[
    #path('',views.intro,name='intro'),
    path('',views.intro1,name='intro1'),
    path('add',views.add,name='add'),
]