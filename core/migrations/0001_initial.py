# Generated by Django 4.0.4 on 2022-05-16 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaDemandaOferta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrecategoria', models.CharField(max_length=30, null=True, unique=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'CategoriaDemandaOferta',
                'verbose_name_plural': 'CategoriaDemandaOferta',
            },
        ),
        migrations.CreateModel(
            name='DemandaPyme',
            fields=[
                ('id_dp', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_dp', models.CharField(max_length=100)),
                ('demandapyme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demandaspyme', to='core.categoriademandaoferta', to_field='nombrecategoria')),
                ('idcategoriademaandaoferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriademandaoferta')),
            ],
            options={
                'verbose_name': 'DemandaPyme',
                'verbose_name_plural': 'DemandaPyme',
            },
        ),
        migrations.CreateModel(
            name='OfertaPyme',
            fields=[
                ('id_op', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion_op', models.CharField(max_length=100)),
                ('idcategoriademandaoferta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriademandaoferta')),
            ],
            options={
                'verbose_name': 'Oferta Pyme',
                'verbose_name_plural': 'Oferta Pyme',
            },
        ),
        migrations.CreateModel(
            name='Pyme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombrepyme', models.CharField(max_length=50, null=True, unique=True)),
                ('rutpyme', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('comuna', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('whatsapp', models.CharField(max_length=15)),
                ('telegram', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Pyme',
                'verbose_name_plural': 'Pyme',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('ofertapyme_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.ofertapyme')),
                ('demandapyme_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.demandapyme')),
            ],
            bases=('core.demandapyme', 'core.ofertapyme'),
        ),
        migrations.AddField(
            model_name='ofertapyme',
            name='idpymeo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombrespymee', to='core.pyme', to_field='nombrepyme'),
        ),
        migrations.AddField(
            model_name='ofertapyme',
            name='ofertapyme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ofertaspyme', to='core.categoriademandaoferta', to_field='nombrecategoria'),
        ),
        migrations.AddField(
            model_name='demandapyme',
            name='idpymed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nombrespyme', to='core.pyme', to_field='nombrepyme'),
        ),
    ]