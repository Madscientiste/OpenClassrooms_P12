# Generated by Django 4.0.3 on 2022-04-29 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
        ('client', '0002_remove_client_email_remove_client_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sales_contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.salesman'),
        ),
    ]
