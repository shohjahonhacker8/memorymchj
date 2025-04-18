# Generated by Django 4.2.16 on 2025-04-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yangi_ilova', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Kontakt',
                'verbose_name_plural': 'Kontaktlar',
            },
        ),
        migrations.DeleteModel(
            name='Ilova',
        ),
    ]
