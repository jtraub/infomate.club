# Generated by Django 2.2.8 on 2020-01-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0015_board_curator_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardfeed',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]