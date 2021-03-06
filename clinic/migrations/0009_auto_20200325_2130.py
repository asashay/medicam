# Generated by Django 3.0.4 on 2020-03-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_doctor_utc_offset'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='text_only',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('against_patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reported_by', to='clinic.Patient')),
                ('by_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinic.Doctor')),
                ('by_patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clinic.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('text', models.TextField()),
                ('sent', models.DateTimeField(auto_now_add=True)),
                ('read', models.DateTimeField(blank=True, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.Doctor', to_field='uuid')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.Patient', to_field='uuid')),
            ],
        ),
    ]
