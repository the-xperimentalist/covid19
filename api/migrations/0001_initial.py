# Generated by Django 3.0.5 on 2020-04-12 02:55

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('latitude', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=16)),
                ('longitude', models.CharField(max_length=16)),
                ('green', models.ManyToManyField(related_name='green_users', to='api.AppUser')),
                ('red', models.ManyToManyField(related_name='red_users', to='api.AppUser')),
                ('yellow', models.ManyToManyField(related_name='yellow_users', to='api.AppUser')),
            ],
        ),
    ]
