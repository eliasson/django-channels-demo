import random

from django.core.management import BaseCommand
from faker import Factory

from ...models import Foo, Bar

fake = Factory.create()


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(20):
            foo = Foo(text=fake.bs())
            foo.save()
            if random.choice([True, False]):
                Bar(foo=foo, text=fake.catch_phrase()).save()
