from django.db import models


class Foo(models.Model):
    created = models.DateTimeField('created', auto_now_add=True, blank=True)
    text = models.CharField('text', max_length=1024)

    # Related: bars (Bar)

    def __str__(self):
        return self.text


class Bar(models.Model):
    foo = models.ForeignKey(Foo, null=True, blank=True, related_name='bars')
    created = models.DateTimeField('created', auto_now_add=True, blank=True)
    text = models.CharField('text', max_length=1024)

    def __str__(self):
        return self.text


class ChatMessage(models.Model):
    message = models.CharField('text', max_length=1024)

    def __str__(self):
        return self.message
