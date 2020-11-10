# Generated by Django 2.2.5 on 2020-11-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submitattendance',
            name='place',
            field=models.IntegerField(choices=[(1, '東京'), (2, '大阪'), (3, '名古屋'), (4, '福岡'), (5, '札幌'), (6, '沖縄')], default=None, verbose_name='出勤場所名'),
        ),
    ]
