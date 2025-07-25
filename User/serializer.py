from rest_framework import serializers
from .models import User
from .utils import validate_serilizers_data

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            "username":{"validators":[]},
            "email":{"validators":[]}
        }

    def validate(self, attrs):
        result = str(validate_serilizers_data(attrs=attrs))
        db_username = User.objects.filter(username = attrs.get('username')).exists()
        db_email = User.objects.filter(email = attrs.get('email')).exists()

        if result != 'Test Ok':
            raise serializers.ValidationError(result)
        
        if db_username:
            raise serializers.ValidationError('Ushbu username foydalanuvchisi ro`yxatda mavjud')

        if db_email:
            raise serializers.ValidationError('Ushbu email manzili allaqachon ro`yxatga olingan')
        print('Hello')
        return attrs
    
    def create(self, validated_data):

        validated_data.pop('confirm_password')
        validated_data['is_ban'] = False
        validated_data['role'] = 'student'
            
        return User.objects.create(**validated_data)
    

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username, password=password).first()

        if user:
            attrs['user'] = user
            return attrs
        raise serializers.ValidationError('Username yoki parol xato, qaytadan urinib ko`ring')