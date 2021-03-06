# Generated by Django 3.1.1 on 2020-09-16 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=500)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.movies')),
            ],
        ),
    ]
