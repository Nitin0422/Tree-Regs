# Generated by Django 4.2.5 on 2023-09-20 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RS', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ctrs',
            old_name='rree_id',
            new_name='tree_id',
        ),
    ]
