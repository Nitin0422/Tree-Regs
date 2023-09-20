# Generated by Django 4.2.5 on 2023-09-19 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LandDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ETRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_name', models.CharField(max_length=200)),
                ('tree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RS.landdetails')),
            ],
        ),
        migrations.CreateModel(
            name='CTRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree_name', models.CharField(max_length=200)),
                ('rree_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RS.landdetails')),
            ],
        ),
    ]
