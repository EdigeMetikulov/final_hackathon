from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from apps.account.serializers import RegistrationSerializer, ForgetPasswordSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.account.services.utils import send_new_password

User = get_user_model()


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = "User registered!"
            return Response(message)


class ActivationView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('your account is sucessfully activated!', status=status.HTTP_200_OK)


class ForgetPasswordView(APIView):

    def post(self, request):
        data = request.POST
        serializer = ForgetPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user: User = User.objects.get(email=email)
        new_password = user.generate_activation_code(10, 'qwergafsg57')
        user.set_password(new_password)
        user.save()
        send_new_password(email, new_password)
        return Response({'message': 'your new password was send to email'}, status=status.HTTP_200_OK)
