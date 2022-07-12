# Generated by Django 4.0.5 on 2022-07-10 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_remaniningstock_product_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SIZE_Prod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('75_85', 'XS'), ('100_120', 'XSS'), ('130_140', 'SXS'), ('XS', 'XS'), ('XS', 'XS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='S', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='venCode',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.size_prod'),
        ),
    ]
