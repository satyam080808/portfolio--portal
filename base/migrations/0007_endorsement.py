# Generated by Django 5.1.6 on 2025-02-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
