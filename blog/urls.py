from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home-page'),
    path('blog/', views.BlogListView.as_view(), name='blog-page'),
    path('blog/<int:pk>', views.BlogDeatailView.as_view(), name='single-page'),
]

