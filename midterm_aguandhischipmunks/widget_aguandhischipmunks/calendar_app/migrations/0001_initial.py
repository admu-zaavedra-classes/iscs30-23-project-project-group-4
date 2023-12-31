# Generated by Django 4.1.7 on 2023-03-05 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('onsite', 'ONSITE'), ('online', 'ONLINE'), ('hybrid', 'HYBRID')], default='onsite', max_length=50)),
                ('venue', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_datetime', models.DateTimeField(max_length=50)),
                ('activity', models.CharField(max_length=50)),
                ('estimated_hours', models.FloatField(max_length=50)),
                ('course', models.CharField(default='', max_length=69)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.location')),
            ],
        ),
    ]
