# Generated by Django 2.0.3 on 2020-12-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compuesto', models.CharField(blank=True, max_length=40, null=True)),
                ('marca', models.CharField(blank=True, max_length=40, null=True)),
                ('presentacion', models.CharField(max_length=40, null=True)),
                ('contenido', models.CharField(max_length=40, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
