# Generated by Django 3.0.2 on 2020-02-05 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TUTRReg', '0006_auto_20200204_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dean',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='TUTRReg.Person'),
        ),
    ]
