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
    Icon, Service, Diagram
)


class IconSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Icon
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        else:
            return obj.image.url


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


class StepSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Step
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            if request is not None:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class AboutServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutServiceImage
        fields = '__all__'


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


class DiagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagram
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    content_blocks = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'

    def get_content_blocks(self, obj):
        blocks = []
        request = self.context.get('request')
        for block in obj.content_blocks.all():
            if isinstance(block, IconsBlock):
                serializer = IconsBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            elif isinstance(block, SliderBlock):
                serializer = SliderBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            elif isinstance(block, StepBlock):
                serializer = StepBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            elif isinstance(block, AboutService):
                serializer = AboutServiceSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            elif isinstance(block, ImagesBlock):
                serializer = ImagesBlockSerializer(block, context={'request': request})
                blocks.append(serializer.data)
            elif isinstance(block, Diagram):
                serializer = DiagramSerializer(block, context={'request': request})
                blocks.append(serializer.data)
        return blocks


class ServicePageSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServicePage
        fields = '__all__'

