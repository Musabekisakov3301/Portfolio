from django.urls import path
from .views import PagesListView, PagesDetailView, LangingPageView

urlpatterns = [
    path('page/', PagesListView , name='pages_list'),
    path('<int:pk>/', PagesDetailView.as_view(),name='pages_detail'),
    path('main/', LangingPageView.as_view(), name='main'),
    #path('page/', PagesListView.as_view(), name='pages_list'),
  
   
]