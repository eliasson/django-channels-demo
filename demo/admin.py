from django.contrib import admin
from .models import Foo, Bar, ChatMessage


admin.site.register(Foo)
admin.site.register(Bar)
admin.site.register(ChatMessage)
