# Generated by Django 5.0.6 on 2024-07-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_cours_chapitre'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='create_on',
            field=models.DateField(blank=True, null=True, verbose_name='date de creation'),
        ),
    ]
