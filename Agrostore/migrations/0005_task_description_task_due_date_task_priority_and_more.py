# Generated by Django 5.1.2 on 2024-11-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agrostore', '0004_alter_sale_employee_delete_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=150),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='Task', max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('not approved', 'Not approved'), ('pending', 'Pending'), ('complete', 'Complete'), ('overdue', 'Overdue')], default='Pending', max_length=150),
        ),
    ]
