from django.urls import path
from . import views
from .views import PlayerAddWizard

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('access/', views.access, name='access'),
    path('mercato/', views.mercato, name='mercato'),
    path('/accounts/login/', views.login_user, name='login'),
    path('add_player/',PlayerAddWizard.as_view(),name='add-player'),
    path('clubs/', views.clubs, name='clubs'),
    path('clubs/<pk>', views.club, name='club'),
    
]
