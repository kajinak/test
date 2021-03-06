# Generated by Django 2.1.7 on 2019-03-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familydata', '0003_auto_20190319_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('package', models.CharField(max_length=10)),
                ('news_subscribe', models.BooleanField()),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('date_apply', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
