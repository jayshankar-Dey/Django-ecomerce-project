# Generated by Django 4.2 on 2023-10-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_odders'),
    ]

    operations = [
        migrations.CreateModel(
            name='odderss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(max_length=20)),
                ('pid', models.IntegerField(max_length=20)),
                ('user', models.IntegerField(max_length=20)),
                ('pname', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=200)),
                ('payment', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('25', 'order'), ('50', 'shipped'), ('75', 'out for delivary'), ('100', 'deliverd')], default='25', max_length=20)),
                ('order', models.CharField(default='order', max_length=20)),
                ('address', models.CharField(max_length=240)),
            ],
        ),
        migrations.DeleteModel(
            name='odders',
        ),
    ]
