# Generated by Django 4.2.4 on 2023-08-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl_app', '0003_remove_snippet_shareable_url_snippet_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NiftyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
