# Generated by Django 3.0.4 on 2020-03-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alternatif', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alternatif',
            name='c3',
            field=models.IntegerField(choices=[(1, 'KURANG MENDUKUNG'), (2, 'CUKUP MENDUKUNG'), (3, 'SANGAT MENDUKUNG')], default=1),
        ),
        migrations.AlterField(
            model_name='alternatif',
            name='c4',
            field=models.IntegerField(choices=[(1, 'SANGAT PRIORITAS'), (2, 'PRIORITAS'), (3, 'KURANG PRIORITAS')], default=1),
        ),
        migrations.AlterField(
            model_name='alternatif',
            name='c5',
            field=models.IntegerField(choices=[(1, 'SULIT DIPEROLEH'), (2, 'SEDIKIT MUDAH DIPEROLEH'), (3, 'SANGAT MUDAH DIPEROLEH')], default=1),
        ),
    ]
