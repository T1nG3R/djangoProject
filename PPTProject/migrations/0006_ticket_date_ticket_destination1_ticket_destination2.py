# Generated by Django 4.2.1 on 2023-05-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPTProject', '0005_ticket_alter_profile_firstname_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='destination1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='ticket',
            name='destination2',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
