# Generated by Django 4.1 on 2023-08-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_alter_product_options_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="thumbnail",
            field=models.ImageField(
                blank=True, null=True, upload_to="uploads/product_images/thumbnail/"
            ),
        ),
    ]
