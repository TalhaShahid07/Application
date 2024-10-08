# Generated by Django 5.1 on 2024-09-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuser', '0008_alter_user_full_access_alter_user_modified_access'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='locations',
        ),
        migrations.AddField(
            model_name='user',
            name='location_ids',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_access',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_access',
            field=models.BooleanField(default=True),
        ),
    ]
