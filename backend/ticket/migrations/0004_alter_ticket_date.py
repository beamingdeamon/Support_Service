# Generated by Django 4.0 on 2021-12-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_ticketmessage_ticket_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
