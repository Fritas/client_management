# Generated by Django 2.1.5 on 2019-01-26 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=7)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descont', models.DecimalField(decimal_places=2, max_digits=5)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='trade.Person')),
            ],
        ),
    ]
