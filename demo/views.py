from channels import Channel
from django.http import HttpResponse
from django.views.generic import ListView, View

from .models import Foo


class HomeView(ListView):
    context_object_name = 'objects'
    template_name = 'demo/foo.html'

    def get_queryset(self):
        return Foo.objects.all()


class FakeChat(View):
    def get(self, *args, **kwargs):
        Channel("chat-messages").send({"message": 'Nonsense', })
        return HttpResponse(status=200, content='OK')
