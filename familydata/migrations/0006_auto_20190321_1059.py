# Generated by Django 2.1.7 on 2019-03-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydata', '0005_auto_20190321_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyapply',
            name='package',
            field=models.CharField(choices=[('standart', 'Standart'), ('gold', 'Gold'), ('vip', 'Vip')], default='vip', max_length=10),
        ),
    ]
