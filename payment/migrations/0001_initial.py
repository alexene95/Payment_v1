# Generated by Django 3.1.1 on 2020-09-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreditCardNumber', models.CharField(max_length=100)),
                ('CardHolder', models.CharField(max_length=100)),
                ('ExpirationDate', models.DateField()),
                ('SecurityCode', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
