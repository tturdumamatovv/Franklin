from rest_framework import serializers

from .models import (
    AboutPage,
    ImagesBlock,
    Image,
    SliderBlock,
    Slide,
    IconsBlock,
    Icon,
    Video
)


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class SlideSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Slide
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class IconSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Icon
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class ImagesBlockSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ImagesBlock
        fields = '__all__'


class SliderBlockSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = SliderBlock
        fields = '__all__'


class IconsBlockSerializer(serializers.ModelSerializer):
    icons = IconSerializer(many=True, read_only=True)

    class Meta:
        model = IconsBlock
        fields = '__all__'


class AboutPageSerializer(serializers.ModelSerializer):
    content_blocks = serializers.SerializerMethodField()

    class Meta:
        model = AboutPage
        fields = '__all__'

    def get_content_blocks(self, obj):
        blocks = []
        request = self.context.get('request')
        for block in obj.content_blocks.all():
            if isinstance(block, ImagesBlock):
                serializer = ImagesBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            if isinstance(block, SliderBlock):
                serializer = SliderBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            if isinstance(block, IconsBlock):
                serializer = IconsBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
        return blocks


class VideoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'url']

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.url.url)

