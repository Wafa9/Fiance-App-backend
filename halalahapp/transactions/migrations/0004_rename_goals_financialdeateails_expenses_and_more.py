# Generated by Django 4.0.1 on 2022-03-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_category_alter_transaction_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialdeateails',
            old_name='goals',
            new_name='expenses',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('BALANCE', 'BALANCE'), ('SAVING', 'SAVING'), ('LOANS', 'LOANS'), ('INCOME', 'INCOME'), ('EXPENSES', 'EXPENSES')], max_length=255),
        ),
    ]
