# Generated by Django 3.0.7 on 2020-07-09 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200707_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='cities',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sig',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
