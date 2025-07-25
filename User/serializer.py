from rest_framework import serializers
from .models import User
from .utils import validate_serilizers_data

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']

    def validate(self, attrs):
        result = str(validate_serilizers_data(**attrs))
        db_username = User.objects.filter(username = attrs['username']).exists()
        db_email = User.objects.filter(email = attrs['email']).exists()

        if result != 'Test Ok':
            raise serializers.ValidationError(result)
        
        if db_username:
            raise serializers.ValidationError('Ushbu username foydalanuvchisi ro`yxatda mavjud')

        if db_email:
            raise serializers.ValidationError('Ushbu email manzili allaqachon ro`yxatga olingan')

        return attrs
    
    def create(self, validated_data):

        validated_data.pop('confirm_password')
        validated_data['is_ban'] = False
        validated_data['role'] = 'student'
            
        return User.objects.create(**validated_data)