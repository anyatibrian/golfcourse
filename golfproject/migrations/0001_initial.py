# Generated by Django 2.1.4 on 2019-03-06 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea_time', models.TimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('play_type', models.CharField(choices=[('professional', 'professional'), ('Handicap', 'Handicap')], default='professional', max_length=20, null=True)),
                ('play_levels', models.CharField(choices=[('professional', 'professional'), ('Handicap', 'Handicap')], default='professional', max_length=20, null=True)),
                ('Handicaps', models.CharField(choices=[('men', 'men'), ('women', 'women')], default='men', max_length=20, null=True)),
                ('men_handicap', models.CharField(max_length=20, null=True)),
                ('women_handicap', models.CharField(default='None', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_fee', models.CharField(max_length=60)),
                ('images', models.ImageField(default='golf', upload_to='images')),
                ('description', models.TextField(default='please enter the tournament description here', max_length=300)),
                ('venue', models.CharField(default='entebbe golf club', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(default='male', max_length=100)),
                ('address', models.CharField(default='kamapala', max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('member_category', models.CharField(max_length=100)),
                ('image', models.ImageField(default='avatar.jpg', upload_to='profile_pics')),
            ],
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='golfproject.Tournament'),
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
