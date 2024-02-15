from django.urls import path
from . import views
from .views import PlayerAddWizard

urlpatterns = [
    path('', views.home, name='home'),
    path('core/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('core/register/', views.register_user, name='register'),
    path('core/access/', views.access, name='access'),
    path('core/mercato/', views.mercato, name='mercato'),
    path('core/add_player/',PlayerAddWizard.as_view(),name='add-player'),
    path('core/clubs/', views.clubs, name='clubs'),
    path('core/clubs/<pk>', views.club, name='club'),
    
]
