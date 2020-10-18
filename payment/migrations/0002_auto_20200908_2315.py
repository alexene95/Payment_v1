# Generated by Django 3.1.1 on 2020-09-08 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='pay',
            name='CreditCardNumber',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='pay',
            name='SecurityCode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
