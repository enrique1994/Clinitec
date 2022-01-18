# Generated by Django 2.0.3 on 2020-12-16 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_medicamento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('rfc', models.CharField(blank=True, max_length=20, null=True)),
                ('fisica_moral', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]