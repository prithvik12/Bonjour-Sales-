# Generated by Django 4.0.2 on 2022-03-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_employee_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='STORES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storename', models.CharField(max_length=100)),
                ('Branch', models.CharField(max_length=300)),
            ],
        ),
    ]
