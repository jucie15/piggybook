# Generated by Django 2.2.2 on 2019-07-11 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('crawled_at', models.DateTimeField()),
            ],
        ),
    ]
