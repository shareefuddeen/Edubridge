# Generated by Django 5.1.1 on 2024-12-22 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_alter_enrollment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set(),
        ),
    ]
