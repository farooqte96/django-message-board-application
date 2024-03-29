# Generated by Django 2.0.7 on 2019-07-09 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
                ('sender', models.CharField(max_length=264, unique=True)),
                ('url', models.URLField(unique=True)),
            ],
        ),
    ]
