# Generated by Django 3.0 on 2019-12-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HourSteps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_steps', models.IntegerField()),
                ('time', models.DateTimeField()),
            ],
        ),
    ]