# Generated by Django 3.1.6 on 2021-05-29 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20210529_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='DOB',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='seminar',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]