# Generated by Django 5.0.1 on 2024-01-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0003_flashcarddesafio_desafio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('F', 'Feito'), ('NF', 'Não Feito')], max_length=2)),
            ],
        ),
    ]
