from rest_framework import serializers

from .models import (
    ServicePage,
    IconsBlock,
    SliderBlock,
    StepBlock,
    AboutService,
    ImagesBlock,
    Image,
    Slide,
    Step,
    AboutServiceImage,
    Icon
)


class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields = '__all__'


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'


class AboutServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutServiceImage
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class IconsBlockSerializer(serializers.ModelSerializer):
    icons = IconSerializer(many=True, read_only=True)

    class Meta:
        model = IconsBlock
        fields = '__all__'


class SliderBlockSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(many=True, read_only=True)

    class Meta:
        model = SliderBlock
        fields = '__all__'


class StepBlockSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = StepBlock
        fields = '__all__'


class AboutServiceSerializer(serializers.ModelSerializer):
    images = AboutServiceImageSerializer(many=True, read_only=True)

    class Meta:
        model = AboutService
        fields = '__all__'


class ImagesBlockSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = ImagesBlock
        fields = '__all__'


class ServicePageSerializer(serializers.ModelSerializer):
    content_blocks = serializers.SerializerMethodField()

    class Meta:
        model = ServicePage
        fields = '__all__'

    def get_content_blocks(self, obj):
        blocks = []
        for block in obj.content_blocks.all():
            if isinstance(block, IconsBlock):
                serializer = IconsBlockSerializer(block)
                blocks.append(serializer.data)
            elif isinstance(block, SliderBlock):
                serializer = SliderBlockSerializer(block)
                blocks.append(serializer.data)
            elif isinstance(block, StepBlock):
                serializer = StepBlockSerializer(block)
                blocks.append(serializer.data)
            elif isinstance(block, AboutService):
                serializer = AboutServiceSerializer(block)
                blocks.append(serializer.data)
            elif isinstance(block, ImagesBlock):
                serializer = ImagesBlockSerializer(block)
                blocks.append(serializer.data)
        return blocks
