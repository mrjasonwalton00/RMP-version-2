# Generated by Django 4.1.3 on 2022-11-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_review_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='courses',
            field=models.CharField(max_length=800, null=True),
        ),
    ]
