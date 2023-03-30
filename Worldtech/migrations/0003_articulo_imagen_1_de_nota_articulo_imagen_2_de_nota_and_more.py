# Generated by Django 4.1.7 on 2023-03-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Worldtech', '0002_articulo_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen_1_de_nota',
            field=models.ImageField(blank=True, null=True, upload_to='publicaciones'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen_2_de_nota',
            field=models.ImageField(blank=True, null=True, upload_to='publicaciones'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='imagen_principal',
            field=models.ImageField(blank=True, null=True, upload_to='publicaciones'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='breve_descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion_articulo_conclusion',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion_articulo_desarrollo',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='descripcion_articulo_inicio',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='titulo_articulo',
            field=models.CharField(max_length=100),
        ),
    ]
