# Generated by Django 3.1.1 on 2020-11-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorer', '0002_auto_20200917_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('body', models.CharField(max_length=12000)),
                ('image', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(default='teacher@teacher.com', max_length=254, unique=True)),
                ('fName', models.CharField(max_length=50)),
                ('lName', models.CharField(max_length=50)),
                ('bio', models.CharField(max_length=500)),
                ('profile', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
