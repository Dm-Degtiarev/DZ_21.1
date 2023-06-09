"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *


app_name = CatalogConfig.name


urlpatterns = [
    path('', IndexView.as_view()),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_item'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<blog_slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<blog_slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog/<blog_slug>/', BlogDetailView.as_view(), name='blog_detail'),

]
