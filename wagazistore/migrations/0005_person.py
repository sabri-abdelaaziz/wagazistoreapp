# Generated by Django 2.1.15 on 2023-06-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagazistore', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
