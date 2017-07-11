from rest_framework import serializers

from member.models import User

__all__ = (
    'UserSerializer',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )


class UserCreationSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
    )
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'password',
        )

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('Username already exists')
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def save(self, *args, **kwargs):
        username = self.validate_data.get('username', '')
        password = self.validated_data.get('password', '')

        user = User.objects.create_user(
            username=username,
            password=password
        )
        return user
