# Generated by Django 5.1.2 on 2024-10-29 04:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WalletAdminActions',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False)),
                ('admins_actions_date', models.DateField(default=django.utils.timezone.now)),
                ('admins_actions_username', models.CharField()),
                ('admins_actions', models.CharField()),
                ('admins_actions_name', models.CharField()),
                ('admin_email', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'wallet_admins_actions',
                'managed': False,
            },
        ),
    ]
