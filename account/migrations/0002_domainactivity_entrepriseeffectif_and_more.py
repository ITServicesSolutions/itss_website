# Generated by Django 4.1.2 on 2022-10-23 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DomainActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'DomainActivity',
                'verbose_name_plural': 'DomainActivitys',
            },
        ),
        migrations.CreateModel(
            name='EntrepriseEffectif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_range', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'EntrepriseEffectif',
                'verbose_name_plural': 'EntrepriseEffectifs',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='contact_method_email',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='contact_method_phone',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.CreateModel(
            name='Entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('link', models.URLField()),
                ('date_saved', models.DateTimeField(auto_now_add=True)),
                ('date_last_activity', models.DateTimeField(auto_now=True)),
                ('contact_method_email', models.BooleanField(blank=True, default=True)),
                ('contact_method_phone', models.BooleanField(blank=True, default=True)),
                ('domain', models.ManyToManyField(to='account.domainactivity')),
                ('effectif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.entrepriseeffectif')),
            ],
            options={
                'verbose_name': 'Entreprise',
                'verbose_name_plural': 'Entreprises',
            },
        ),
    ]
