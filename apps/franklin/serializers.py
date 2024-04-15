from rest_framework import serializers


class PageSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    sub_title = serializers.CharField(max_length=200, allow_null=True, required=False)
    title_en = serializers.CharField(max_length=200)
    sub_title_en = serializers.CharField(max_length=200, allow_null=True, required=False)


class AllPagesSerializer(serializers.Serializer):
    about_page = PageSerializer()
    contact = PageSerializer()
    portfolio_page = PageSerializer()
    service_page = PageSerializer()
