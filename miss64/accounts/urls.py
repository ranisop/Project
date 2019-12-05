from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),       # 장고에서 약속한 주소
    path('login/', views.login, name='login'),          # 장고에서 약속한 주소
    path('logout/', views.logout, name='logout'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
    path('password/', views.password, name='password'),
    
]