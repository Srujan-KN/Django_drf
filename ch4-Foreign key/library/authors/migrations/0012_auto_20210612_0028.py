# Generated by Django 3.1.2 on 2021-06-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0011_auto_20210612_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(db_column='f', on_delete=django.db.models.deletion.DO_NOTHING, to='authors.authors'),
        ),
    ]
