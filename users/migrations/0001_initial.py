# Generated by Django 2.2 on 2022-04-22 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=200)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buddy', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buddy', to=settings.AUTH_USER_MODEL)),
                ('goals', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.Goal')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
