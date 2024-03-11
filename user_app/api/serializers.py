from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'write_only':True})
    class Meta:
        model = User
        fields = ['username','email', 'password', 'password_confirmation']
        extra_kwargs ={'password':{'write_only':True},}

    def save(self, *args, **kwargs):
        password = self.validated_data['password']
        cnf_password = self.validated_data['password_confirmation'] 
        if password!= cnf_password:
            raise serializers.ValidationError({'password_confirmation': 'Passwords do not match'})
        elif User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})
        
        user = User.objects.create(username=self.validated_data['username'],
                                   email=self.validated_data['email'])
        user.set_password(password)
        user.save()
        return user