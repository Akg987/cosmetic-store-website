# Generated by Django 5.1 on 2024-09-02 16:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cosmetics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('caption', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='files/cover')),
            ],
        ),
        migrations.CreateModel(
            name='ask',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('caption', models.CharField(max_length=2000)),
                ('Created', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سوال',
                'verbose_name_plural': 'سوال ها',
            },
        ),
        migrations.CreateModel(
            name='CommentAsk',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=2000)),
                ('Created', models.DateTimeField()),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.ask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'جواب سوالات',
                'verbose_name_plural': 'جواب ها',
            },
        ),
    ]
