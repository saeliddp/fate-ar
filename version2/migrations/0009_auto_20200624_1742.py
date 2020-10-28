# Generated by Django 2.2.6 on 2020-06-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version2', '0008_respondent_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='num_fake',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='order',
            field=models.CharField(default='1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20', max_length=70),
        ),
    ]
