# Generated by Django 4.0.2 on 2022-02-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMPLOYEE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=300)),
                ('timings', models.IntegerField()),
                ('salaryperday', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
