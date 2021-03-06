# Generated by Django 2.1.5 on 2019-01-26 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_doc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveSmallIntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person_photos')),
                ('doc', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trade.Document')),
            ],
        ),
    ]
