from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@1jz.ru',
            first_name='test',
            last_name='1jz',
            is_staff=True,
            is_superuser=True

        )

        user.set_password('12345')
        user.save()