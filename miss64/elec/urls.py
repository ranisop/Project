from django.urls import path
from . import views

app_name = 'elec'

urlpatterns = [
    path('', views.index, name='index'), # /elec/   -> 메인페이지
    path('brand/', views.brand_select, name='brand_select'),
    path('home/<int:brand_id>/', views.home_select, name='home_select'),
    path('middle/<int:brand_id>/<int:home_id>/', views.mid_select, name='mid_select'),
    path('model/<int:brand_id>/<int:home_id>/<int:middle_id>/models', views.model, name='model'),
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result'),
    path('<int:brand_id>/<int:home_id>/<int:middle_id>/<int:pk>/like/', views.like, name='like'),
    path('like_page/', views.like_page, name='like_page'),
]