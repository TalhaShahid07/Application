# Generated by Django 5.1 on 2024-09-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0002_alter_shiftattendance_clocked_in_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='assignedshift',
            options={'ordering': ['-create_date'], 'verbose_name': 'Assigned Shift', 'verbose_name_plural': 'Assigned Shifts'},
        ),
        migrations.AlterField(
            model_name='assignedshift',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shiftattendance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
