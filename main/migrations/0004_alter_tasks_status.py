# Generated by Django 5.2 on 2025-06-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tasks_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')], default='New', max_length=20),
        ),
    ]
