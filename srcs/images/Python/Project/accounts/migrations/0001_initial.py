# Generated by Django 4.2.11 on 2024-03-19 09:52

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('PreferredLanguage', models.CharField(default='English', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, related_name='usermodel_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usermodel_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tfa_enabled', models.BooleanField(default=False)),
                ('otp_base32', models.CharField(max_length=255, null=True)),
                ('token', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=151)),
                ('picUrl', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile1_(42)_(42).png', null=True, upload_to='')),
                ('api_token', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('tournament', models.IntegerField(default=0)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.JSONField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='game', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('player1score', models.IntegerField(blank=True, null=True)),
                ('player2score', models.IntegerField(blank=True, null=True)),
                ('loserscore', models.IntegerField(blank=True, null=True)),
                ('winnerscore', models.IntegerField(blank=True, null=True)),
                ('loser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to=settings.AUTH_USER_MODEL)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
