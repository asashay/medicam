# Generated by Django 3.0.4 on 2020-04-04 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('clinic', '0025_auto_20200404_0045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callsummary',
            options={'verbose_name_plural': 'call summaries'},
        ),
        migrations.AddField(
            model_name='callsummary',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
    ]
