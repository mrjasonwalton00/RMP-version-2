# Generated by Django 4.1.3 on 2022-11-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_review_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='picture',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
