from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=20)
    objects = models.Manager()

    def __str__(self):
        return self.nome


class Flashcard(models.Model):
    DIFICULDADE_CHOICES = (('D', 'Difícil'), ('M', 'Médio'), ('F', 'Fácil'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pergunta = models.CharField(max_length=100)
    resposta = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)
    objects = models.Manager()

    def __str__(self):
        return self.pergunta

    @property
    def css_dificuldade(self):
        if self.dificuldade == 'F':
            return "flashcard-facil"
        elif self.dificuldade == 'M':
            return 'flashcard-medio'
        elif self.dificuldade == 'D':
            return 'flashcard-dificil'


class FlashcardDesafio(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    respondido = models.BooleanField(default=False)
    acertou = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.flashcard.pergunta


class Desafio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
    quantidade_perguntas = models.IntegerField()
    dificuldade = models.CharField(
        max_length=1, choices=Flashcard.DIFICULDADE_CHOICES
    )
    flashcards = models.ManyToManyField(FlashcardDesafio)
    objects = models.Manager()

    def __str__(self):
        return self.titulo
