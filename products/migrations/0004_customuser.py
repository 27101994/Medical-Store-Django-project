# Generated by Django 4.2.6 on 2023-11-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
