from django.conf import settings
from django.conf.urls.static import static

from .views import ProfileDetail, signup, LoginPage, ProfileChangeDetail

from django.urls import path

urlpatterns = [
    path("<int:pk>/", ProfileDetail.as_view(), name="Profile-detail"),
    path("sign_up/", signup, name="SignUp"),
    path("login/", LoginPage, name="Login"),
    path("change/<int:pk>", ProfileChangeDetail.as_view(), name="ChangeForm")
]
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
