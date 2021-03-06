# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_location', geoposition.fields.GeopositionField(blank=True, max_length=42, null=True, verbose_name='Where you want power to be installed')),
                ('distance', models.IntegerField(default=0, verbose_name='Distance from Transformer')),
                ('receipt_no', models.CharField(blank=True, max_length=30, null=True, verbose_name='Receipt No:')),
                ('location', models.CharField(blank=True, default='here', max_length=50, null=True)),
                ('payment_method', models.CharField(blank=True, choices=[('NOT YET PAID', 'I will pay later'), ('MPESA', 'M-PESA paybill no. 34589'), ('KCB', 'KCB Eldoret branch Account No. 12345670089'), ('CO-OP', 'CO-OPERATIVE bank Account No 09872346875'), ('EQUITY', 'EQUITY bank Account No 83294847829')], max_length=12, null=True, verbose_name='Your convenient payment method')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount Payed')),
                ('installation', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('installed', models.BooleanField(default=False)),
                ('employee', models.ManyToManyField(related_name='employee', to='operation.Employee')),
                ('transformer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transformer', to='operation.Transformer')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PowerApplication',
                'verbose_name_plural': 'PowerApplications',
            },
        ),
    ]
