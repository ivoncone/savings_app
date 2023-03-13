from django.urls import path

from savings import views
from .views import DaysView, SavingsView

urlpatterns = [
	path('savings/', views.SavingsView.as_view()),
	path('days/', views.DaysView.as_view())
]