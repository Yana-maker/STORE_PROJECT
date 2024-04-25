from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='Admin@sky.pro',
            username='admin',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('1234')
        user.save()

        user = User.objects.create(
            email='yanaposelenceva@gmail.com',
            username='admin2',
            is_staff=True,
            is_superuser=False,
            is_active=True,
            role='moderator'
        )

        user.set_password('1234')
        user.save()

        user = User.objects.create(
            email='yanik-092@yandex.ru',
            username='admin3',
            is_staff=False,
            is_superuser=False,
            is_active=True,
        )

        user.set_password('1234')
        user.save()
