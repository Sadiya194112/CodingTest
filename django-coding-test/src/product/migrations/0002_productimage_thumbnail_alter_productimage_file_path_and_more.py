# Generated by Django 5.0.6 on 2024-05-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='thumbnail',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='file_path',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
