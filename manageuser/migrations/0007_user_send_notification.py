# Generated by Django 5.1 on 2024-09-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuser', '0006_alter_user_email_alter_user_full_access_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='send_notification',
            field=models.BooleanField(default=True),
        ),
    ]
