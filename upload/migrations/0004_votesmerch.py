# Generated by Django 2.2.3 on 2019-08-05 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0003_auto_20190802_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotesMerch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='upload.Post')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
