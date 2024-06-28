from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('journals/<int:journal_type_id>/', views.journal_list, name='journal_list'),
    path('journals/<int:journal_type_id>/new/', views.new_journal, name='new_journal'),
    path('journals/<int:id>/', views.journal_detail, name='journal_detail'),
    path('journal/<int:id>/edit/', views.edit_journal, name='edit_journal'),
    path('journal/<int:id>/delete/', views.delete_journal, name='delete_journal'),
    path('journal_type/new/', views.new_journal_type, name='new_journal_type'),
    path('journal_type/<int:id>/edit/', views.edit_journal_type, name='edit_journal_type'),
    path('journal_type/<int:id>/delete/', views.delete_journal_type, name='delete_journal_type'),
]