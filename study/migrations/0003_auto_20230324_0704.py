# Generated by Django 2.2 on 2023-03-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_auto_20230320_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='subject',
            field=models.CharField(choices=[(1, '화면구현'), (2, '구현'), (3, '응용'), (4, '영어'), (5, '분석'), (6, '논술'), (7, '수학'), (8, '국어')], default=None, max_length=4),
        ),
    ]