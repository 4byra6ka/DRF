# Generated by Django 4.2.3 on 2023-07-21 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_course_owner_lesson_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Cсылка на видео'),
        ),
        migrations.CreateModel(
            name='Subscrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscrip', to='course.course', verbose_name='Подписка на курс')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
        ),
    ]
