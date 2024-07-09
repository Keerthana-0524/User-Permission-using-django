# Generated by Django 5.0.6 on 2024-07-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forma',
            old_name='title',
            new_name='field1',
        ),
        migrations.RenameField(
            model_name='forma',
            old_name='content',
            new_name='field2',
        ),
        migrations.RenameField(
            model_name='forma',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='formb',
            old_name='title',
            new_name='field1',
        ),
        migrations.RenameField(
            model_name='formb',
            old_name='content',
            new_name='field2',
        ),
        migrations.RenameField(
            model_name='formb',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='formc',
            old_name='title',
            new_name='field1',
        ),
        migrations.RenameField(
            model_name='formc',
            old_name='content',
            new_name='field2',
        ),
        migrations.RenameField(
            model_name='formc',
            old_name='created_by',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superadmin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_user',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
