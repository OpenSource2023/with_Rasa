from rest_framework import serializers
from .models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(max_length=10, allow_null=True, required=True)
    birth = serializers.DateField(allow_null=True, required=True)
    phone = serializers.CharField(max_length=15, allow_null=True, required=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'password', 'gender', 'birth', 'phone')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        username = validated_data.get('username')
        
        # 이미 존재하는 사용자인지 확인
        existing_user = UserProfile.objects.filter(username=username).first()
        
        if existing_user:
            # 이미 존재하는 사용자에 대한 수정 등의 작업 수행
            existing_user.gender = validated_data.get('gender', existing_user.gender)
            existing_user.birth = validated_data.get('birth', existing_user.birth)
            existing_user.phone = validated_data.get('phone', existing_user.phone)
            existing_user.save()
            
            return existing_user
        else:
            # 이미 존재하지 않는 사용자인 경우 새로 생성
            return super().create(validated_data)