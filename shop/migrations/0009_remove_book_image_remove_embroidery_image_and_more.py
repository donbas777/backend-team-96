# Generated by Django 5.1 on 2024-08-30 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_bookimage_title_alter_embroidery_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='image',
        ),
        migrations.RemoveField(
            model_name='embroidery',
            name='image',
        ),
        migrations.AlterField(
            model_name='bookimage',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.book'),
        ),
        migrations.AlterField(
            model_name='embroideryimage',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.embroidery'),
        ),
    ]
