# Generated by Django 4.1.7 on 2023-03-06 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_alter_widgetuser_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=1000)),
                ('pub_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Published Date and Time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.widgetuser')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=1000)),
                ('pub_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Published Date and Time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.widgetuser')),
                ('forum_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forumpost')),
            ],
        ),
    ]
