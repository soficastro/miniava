# Generated by Django 2.2.3 on 2019-08-17 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190817_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('released_date', models.DateField(blank=True, null=True, verbose_name='Data de liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(blank=True, verbose_name='Vídeo embedded')),
                ('file', models.FileField(blank=True, upload_to='lessons/materials', verbose_name='Arquivo')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='materials', to='courses.Lesson', verbose_name='Aula')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
        ),
    ]
