# Generated by Django 3.2.3 on 2021-05-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hat_Kodu', models.FloatField()),
                ('Gun', models.FloatField()),
                ('Saat', models.FloatField()),
                ('Arac_Kimligi', models.FloatField()),
                ('Konum_Bilgisi', models.FloatField()),
                ('Personel_Sicili', models.FloatField()),
                ('Surucu_Performans_Puani', models.FloatField()),
                ('Target', models.CharField(max_length=30)),
            ],
        ),
    ]
