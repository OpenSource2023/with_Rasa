from contextvars import Token
from rest_framework import viewsets, status
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import UserProfile

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 중복 사용자 이름 확인
        username = serializer.validated_data['username']
        existing_user = UserProfile.objects.filter(username=username).first()

        if existing_user:
            # 이미 존재하는 사용자에 대한 에러 응답
            return Response({"error": "Duplicate username"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 중복 확인을 통과한 경우에만 저장
            user_profile = serializer.save()

            # User 객체도 생성
            user_data = {
                'username': serializer.validated_data['username'],
                'password': serializer.validated_data['password'],
            }

            # 중복 확인을 이미 수행했으므로 create_user 대신 create를 사용
            user = UserProfile.objects.create(**user_data)

            # Token 생성
            Token.objects.create(user=user)

            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        serializer.save()
