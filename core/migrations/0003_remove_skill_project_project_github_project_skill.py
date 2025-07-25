# Generated by Django 5.2.3 on 2025-06-22 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_skill_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.URLField(blank=True, default='https://github.com', null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ManyToManyField(blank=True, to='core.skill'),
        ),
    ]
