from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('worksheets/', views.worksheet_list),
    path('note/', views.note_detail),
]