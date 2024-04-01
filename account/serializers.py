from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):
  confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email','password', 'confirm_password']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Password and Confirm_Password Validation
  def validate(self, data):
    password = data.get('password')
    password2 = data.get('confirm_password')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return data

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email']