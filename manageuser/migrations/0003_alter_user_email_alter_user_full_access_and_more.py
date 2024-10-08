# Generated by Django 5.1 on 2024-09-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageuser', '0002_alter_user_full_access_alter_user_modified_access'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='modified_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('EMPLOYEE', 'Employee'), ('MANAGER', 'Manager')], default='EMPLOYEE', max_length=10),
        ),
    ]
