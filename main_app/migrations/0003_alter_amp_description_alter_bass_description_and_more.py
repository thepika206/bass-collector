# Generated by Django 4.1.3 on 2022-11-08 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_amp_rename_model_bass_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amp',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='bass',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bass')),
            ],
        ),
    ]
