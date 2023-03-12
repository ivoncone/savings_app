from django.urls import path

from users import views
from .views import UserSignUpView

urlpatterns = [
	path('signup/', views.UserSignUpView.as_view())
]