# Generated by Django 5.0.1 on 2024-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_remove_userprofile_user_userprofile_name_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
