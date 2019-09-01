# from django.conf.urls import url
# from .views import HelloView
from django.urls import path
from . import views

urlpatterns = [
        # url(r'', HelloView.as_view(), name='index'),
        # path('<int:id>/<nickname>/', views.index, name='index'),
        path('', views.index, name='index'),
        path('create', views.create, name='create'),
        path('edit/<int:num>', views.edit, name='edit'),
        # path('next', views.next, name='next'),
        # path('form', views.form, name='form'),
]
