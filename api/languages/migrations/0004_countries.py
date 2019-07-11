# Generated by Django 2.2.3 on 2019-07-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0003_auto_20190710_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('languages', models.ManyToManyField(to='languages.Language')),
            ],
        ),
    ]
