# Generated by Django 3.0.5 on 2022-05-06 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20220430_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.Pizza')),
            ],
        ),
    ]
