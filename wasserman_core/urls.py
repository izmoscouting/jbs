from django.urls import path
from . import views
from .views import PlayerAddWizard, UpdateAddWizard, CoachAddWizard, AddReportWizard, UpdateReportWizard

urlpatterns = [
    path('', views.home, name='home'),
    path('core/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('core/register/', views.register_user, name='register'),
    path('core/access/', views.access, name='access'),
    path('core/mercato/', views.mercato, name='mercato'),

    path('core/add_player/',PlayerAddWizard.as_view(),name='add-player'),
    path('core/add_report/',AddReportWizard.as_view(),name='add_report'),
    path('core/add_business/',views.add_business,name='add_business'),
    path('core/add_clubs/',views.add_club,name='add_club'),
    path('core/add_agences/',views.add_agence,name='add_agence'),
    path('core/add_contacts/',views.add_contact,name='add_contact'),
    path('core/info_mercato/<player_id>', views.add_info_mercato, name='info_mercato'),
    path('core/add_shortlist/<player_id>', views.add_shortlist, name='add_shortlist'),


    #path('core/add_coach/',CoachAddWizard.as_view(),name='add_coach'),
    path('core/add_player_success/', views.success_view, name='add_player_success'),


    path('core/update_player/<pk>',UpdateAddWizard.as_view(),name='update_player'),
    path('core/update_contact/<pk>',views.update_contact,name='update_contact'),
    path('core/update_agence/<pk>',views.update_agence,name='update_agence'),
    path('core/update_business/<pk>', views.update_business, name='update_business'),
    path('core/update_report/<pk>', UpdateReportWizard.as_view(), name='update_report'),
    path('core/update_club/<pk>', views.update_club, name='update_club'),



    path('core/delete_player/<pk>', views.delete_player, name='delete_player'),
    path('core/delete_club/<pk>', views.delete_club, name='delete_club'),
    path('core/delete_report/<pk>', views.delete_report, name='delete_report'),
    path('core/delete_business/<pk>', views.delete_business, name='delete_business'),
    path('core/delete_agence/<pk>', views.delete_agence, name='delete_agence'),
    path('core/delete_contact/<pk>', views.delete_contact, name='delete_contact'),
    path('core/delete_info/<pk>', views.delete_info, name='delete_info'),
    path('core/delete_target/<pk>', views.delete_target, name='delete_target'),


    path('core/clubs/', views.clubs, name='clubs'),
    path('core/agences/', views.agences, name='agences'),
    path('core/contacts/', views.contacts, name='contacts'),
    path('core/business/', views.business, name='business'),


    path('core/joueur/<pk>', views.joueur, name='joueur'),
    path('core/rapport/<pk>', views.report, name='rapport'),
    path('core/clubs/<pk>', views.club, name='club'),
    path('core/business/<pk>', views.bizi, name='busi'),
    
]
