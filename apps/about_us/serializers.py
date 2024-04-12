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
    class Meta:
        model = Image
        fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


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
        for block in obj.content_blocks.all():
            if isinstance(block, ImagesBlock):
                serializer = ImagesBlockSerializer(block)
                blocks.append(serializer.data)
            if isinstance(block, SliderBlock):
                serializer = SliderBlockSerializer(block)
                blocks.append(serializer.data)
            if isinstance(block, IconsBlock):
                serializer = IconsBlockSerializer(block)
                blocks.append(serializer.data)
        return blocks


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'url']
