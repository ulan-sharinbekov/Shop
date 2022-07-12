# Generated by Django 4.0.5 on 2022-07-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='RemaniningStock',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sum',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('XS', 'XS'), ('XS', 'XS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='S', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='venCode',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
