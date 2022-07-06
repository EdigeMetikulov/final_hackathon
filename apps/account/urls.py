from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from apps.account.views import RegistrationView, ActivationView, ForgetPasswordView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:activation_code>', ActivationView.as_view()),
    # path('login/', LoginView.as_view()),
    # path('token/refresh/', TokenRefreshView.as_view()),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("forget_password/", ForgetPasswordView.as_view()),

]