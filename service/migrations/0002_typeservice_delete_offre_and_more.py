# Generated by Django 4.1.2 on 2022-12-07 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('is_public', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TypeService',
                'verbose_name_plural': 'TypeServices',
            },
        ),
        migrations.DeleteModel(
            name='Offre',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='is_actif',
            new_name='is_public',
        ),
        migrations.AddField(
            model_name='service',
            name='is_principal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.typeservice', verbose_name='Type de service'),
        ),
    ]