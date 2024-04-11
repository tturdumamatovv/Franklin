from rest_framework import serializers

from .models import (
    Address,
    Phone,
    Email,
    SocialLink,
    Application,
    Contact
)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    phones = PhoneSerializer(many=True)
    emails = EmailSerializer(many=True)
    social_links = SocialLinkSerializer(many=True)

    class Meta:
        model = Contact
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
