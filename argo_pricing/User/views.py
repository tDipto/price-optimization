from django.http import HttpResponse
from .serializers import (
    SignUpSerializer,
    CustomTokenObtainPairSerializer,
    ShowUserSerializer,
    OTPVerificationSerializer,
)
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from .models import OTP
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


def index(request):
    return HttpResponse("Hello, world. You're at the User index.")


class SignupAPI(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class SignInAPI(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ShowUserAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = ShowUserSerializer
    lookup_field = "username"

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)


class OTPVerificationAPI(GenericAPIView):
    serializer_class = OTPVerificationSerializer

    def put(self, request, username, *args, **kwargs):
        otp_entry = get_object_or_404(OTP, user__username=username)

        if "otp" not in request.data:
            return Response({"detail": "OTP is required in the request"})

        serializer = self.get_serializer(otp_entry, data=request.data, partial=True)

        if serializer.is_valid():
            if serializer.validated_data.get("otp") == otp_entry.otp:
                otp_entry.is_verified = True
                otp_entry.save()
                return Response({"detail": "OTP verification successful"})
            else:
                return Response({"detail": "Invalid OTP"})
        return Response(serializer.errors)
