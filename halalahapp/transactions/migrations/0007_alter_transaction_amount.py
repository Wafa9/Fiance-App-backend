# Generated by Django 4.0.1 on 2022-03-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0006_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(max_length=255),
        ),
    ]
