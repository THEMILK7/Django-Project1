# Generated by Django 5.0.6 on 2024-07-14 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_chapitre_last_update'),
        ('subscriptions', '0002_alter_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='cours',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.cours'),
        ),
    ]
