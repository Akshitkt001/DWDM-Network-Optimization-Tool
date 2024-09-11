# Generated by Django 5.1.1 on 2024-09-11 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wavelength',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('frequency', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('capacity', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_links', to='network_optimizer.node')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_links', to='network_optimizer.node')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latency', models.FloatField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths_to', to='network_optimizer.node')),
                ('links', models.ManyToManyField(to='network_optimizer.link')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paths_from', to='network_optimizer.node')),
                ('wavelength', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='network_optimizer.wavelength')),
            ],
        ),
    ]
