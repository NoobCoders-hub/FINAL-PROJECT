# Generated by Django 3.2.8 on 2021-12-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='Body_Temperature',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
