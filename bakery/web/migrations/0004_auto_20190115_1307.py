# Generated by Django 2.1.4 on 2019-01-15 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_auto_20181223_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=40)),
                ('delivery_date', models.DateField(blank=True, default=None)),
                ('product_id', models.TextField(blank=True, default=None)),
                ('extra_information', models.TextField(blank=True, default=None)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='diet_list',
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='products',
            field=models.ManyToManyField(blank=True, default='', to='web.Product'),
        ),
    ]
