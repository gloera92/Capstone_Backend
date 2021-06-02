from django.urls import path
from .views import K9List, K9Detail, UserRegistrationView, UserLoginView, UserProfileView


urlpatterns = [
    path("k9list/", K9List.as_view()),
    path("K9detail/<int:pk>/", K9Detail.as_view()),
    path("register/", UserRegistrationView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("profile/", UserProfileView.as_view()),
]