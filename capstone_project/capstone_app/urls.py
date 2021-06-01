from django.urls import path
from .views import UserCreate, LoginView, K9List, K9Detail


urlpatterns = [
    path("register/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("k9list/", K9List.as_view()),
    path("K9detail/<int:pk>/", K9Detail.as_view())
]