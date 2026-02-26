from django.db import models

# Create your models 

Difficulty_Chioces = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]


class Question(models.Model):
    text = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=Difficulty_Chioces,default='medium')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #
        return f"[{self.difficulty}] {self.text:[:50]}..."