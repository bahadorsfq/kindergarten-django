# Generated by Django 5.2 on 2025-06-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_mediareport_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='متن موضوع هفته')),
            ],
        ),
    ]
