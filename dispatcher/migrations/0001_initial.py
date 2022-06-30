# Generated by Django 4.0.4 on 2022-06-28 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
                ('act_type', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/act_images')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/act_files')),
                ('act_processing', models.CharField(choices=[('Ожидание принятия заявки', 'Waiting'), ('Заявки принята', 'Accepted'), ('Заявка возвращена', 'Returned')], default='Ожидание принятия заявки', max_length=25)),
                ('do_until', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]