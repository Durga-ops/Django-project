from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('single_portfolio',views.single_portfolio,name='single_portfolio'),
]