# Generated by Django 5.0.6 on 2024-07-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_chapitre_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/pdfs/'),
        ),
        migrations.AlterField(
            model_name='cours',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='media/video/'),
        ),
    ]
