from rest_framework import viewsets, serializers

from .models import Foo, Bar, ChatMessage


class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
        fields = ('id', 'text',)


class BarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bar
        fields = ('id', 'text',)


class FooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer


class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer


class CompoundFooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
        fields = ('id', 'text', 'bars')

    bars = BarSerializer(many=True, read_only=True)


class CompoundFooViewSet(viewsets.ModelViewSet):
    queryset = Foo.objects.all()
    serializer_class = CompoundFooSerializer


#
# HTTP API for Chat messages
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('id', 'message',)


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer