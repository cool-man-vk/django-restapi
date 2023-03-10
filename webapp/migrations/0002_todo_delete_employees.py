# Generated by Django 4.0 on 2023-01-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('deadline', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='employees',
        ),
    ]
