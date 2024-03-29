# Generated by Django 5.0.1 on 2024-01-19 14:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_delete_status_remove_desafio_flashcards_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='desafio',
            name='flashcards',
            field=models.ManyToManyField(to='flashcard.flashcarddesafio'),
        ),
        migrations.AlterField(
            model_name='desafio',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flashcard.categoria'),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flashcarddesafio',
            name='flashcard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flashcard.flashcard'),
        ),
    ]
