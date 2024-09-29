from rest_framework import serializers

from payroller.users.models import User


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="api:user-detail",
        lookup_field="pk",
    )

    class Meta:
        model = User
        fields = ["name", "url"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get("request", None)
        if request is None:
            ret.pop("url", None)
        return ret


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "name"]

    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
