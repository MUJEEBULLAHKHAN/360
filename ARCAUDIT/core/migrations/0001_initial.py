# Generated by Django 4.1.7 on 2023-02-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arcinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=200, null=True)),
                ('owner', models.CharField(blank=True, max_length=200, null=True)),
                ('contact', models.CharField(blank=True, max_length=200, null=True)),
                ('manager', models.CharField(blank=True, max_length=200, null=True)),
                ('managercont', models.CharField(blank=True, max_length=200, null=True)),
                ('estimate', models.CharField(blank=True, max_length=200, null=True)),
                ('wi1', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='arcloc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='equipinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('it', models.CharField(blank=True, max_length=200, null=True)),
                ('comp', models.CharField(blank=True, max_length=200, null=True)),
                ('access', models.CharField(blank=True, max_length=200, null=True)),
                ('oem', models.CharField(blank=True, max_length=200, null=True)),
                ('guide', models.CharField(blank=True, max_length=200, null=True)),
                ('lift', models.CharField(blank=True, max_length=200, null=True)),
                ('frame', models.CharField(blank=True, max_length=200, null=True)),
                ('four', models.CharField(blank=True, max_length=200, null=True)),
                ('anchor', models.CharField(blank=True, max_length=200, null=True)),
                ('ton', models.CharField(blank=True, max_length=200, null=True)),
                ('oxy', models.CharField(blank=True, max_length=200, null=True)),
                ('resistance', models.CharField(blank=True, max_length=200, null=True)),
                ('heater', models.CharField(blank=True, max_length=200, null=True)),
                ('plasma', models.CharField(blank=True, max_length=200, null=True)),
                ('mig', models.CharField(blank=True, max_length=200, null=True)),
                ('dent', models.CharField(blank=True, max_length=200, null=True)),
                ('air', models.CharField(blank=True, max_length=200, null=True)),
                ('chain', models.CharField(blank=True, max_length=200, null=True)),
                ('charging', models.CharField(blank=True, max_length=200, null=True)),
                ('kit', models.CharField(blank=True, max_length=200, null=True)),
                ('dry', models.CharField(blank=True, max_length=200, null=True)),
                ('hvlp', models.CharField(blank=True, max_length=200, null=True)),
                ('vet', models.CharField(blank=True, max_length=200, null=True)),
                ('booth', models.CharField(blank=True, max_length=200, null=True)),
                ('prep', models.CharField(blank=True, max_length=200, null=True)),
                ('mixing', models.CharField(blank=True, max_length=200, null=True)),
                ('tools', models.CharField(blank=True, max_length=200, null=True)),
                ('toolkit', models.CharField(blank=True, max_length=200, null=True)),
                ('lifts', models.CharField(blank=True, max_length=200, null=True)),
                ('align', models.CharField(blank=True, max_length=200, null=True)),
                ('rise', models.CharField(blank=True, max_length=200, null=True)),
                ('changer', models.CharField(blank=True, max_length=200, null=True)),
                ('balancer', models.CharField(blank=True, max_length=200, null=True)),
                ('lathe', models.CharField(blank=True, max_length=200, null=True)),
                ('notes', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labor', models.CharField(blank=True, max_length=200, null=True)),
                ('part', models.CharField(blank=True, max_length=200, null=True)),
                ('material', models.CharField(blank=True, max_length=200, null=True)),
                ('rent', models.CharField(blank=True, max_length=200, null=True)),
                ('productive', models.CharField(blank=True, max_length=200, null=True)),
                ('support', models.CharField(blank=True, max_length=200, null=True)),
                ('month', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='repairinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(blank=True, max_length=200, null=True)),
                ('nonstruct', models.CharField(blank=True, max_length=200, null=True)),
                ('struct', models.CharField(blank=True, max_length=200, null=True)),
                ('paint', models.CharField(blank=True, max_length=200, null=True)),
                ('ac', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.CharField(blank=True, max_length=200, null=True)),
                ('qc', models.CharField(blank=True, max_length=200, null=True)),
                ('brakes', models.CharField(blank=True, max_length=200, null=True)),
                ('tyre', models.CharField(blank=True, max_length=200, null=True)),
                ('wheel', models.CharField(blank=True, max_length=200, null=True)),
                ('computer', models.CharField(blank=True, max_length=200, null=True)),
                ('adas', models.CharField(blank=True, max_length=200, null=True)),
                ('engine', models.CharField(blank=True, max_length=200, null=True)),
                ('plastic', models.CharField(blank=True, max_length=200, null=True)),
                ('welder', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='workforceinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PPE', models.CharField(blank=True, max_length=200, null=True)),
                ('denter', models.CharField(blank=True, max_length=200, null=True)),
                ('painter', models.CharField(blank=True, max_length=200, null=True)),
                ('elec', models.CharField(blank=True, max_length=200, null=True)),
                ('staff', models.CharField(blank=True, max_length=200, null=True)),
                ('workbays', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.CharField(blank=True, max_length=200, null=True)),
                ('nonbody', models.CharField(blank=True, max_length=200, null=True)),
                ('sqm', models.CharField(blank=True, max_length=200, null=True)),
                ('insurance', models.CharField(blank=True, max_length=200, null=True)),
                ('walkin', models.CharField(blank=True, max_length=200, null=True)),
                ('fleet', models.CharField(blank=True, max_length=200, null=True)),
                ('park', models.CharField(blank=True, max_length=200, null=True)),
                ('recep', models.CharField(blank=True, max_length=200, null=True)),
                ('wash', models.CharField(blank=True, max_length=200, null=True)),
                ('washstaff', models.CharField(blank=True, max_length=200, null=True)),
                ('scrap', models.CharField(blank=True, max_length=200, null=True)),
                ('newpart', models.CharField(blank=True, max_length=200, null=True)),
                ('oilstorage', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
