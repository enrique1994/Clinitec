# Generated by Django 2.0.3 on 2020-12-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('tipo', models.IntegerField(null=True)),
                ('password', models.CharField(blank=True, max_length=75)),
                ('usuario', models.CharField(blank=True, max_length=40)),
                ('foto', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
