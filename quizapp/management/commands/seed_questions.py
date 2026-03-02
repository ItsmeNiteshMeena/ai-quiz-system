from django.core.management.base import BaseCommand
from quizapp.models import Question, Choice

DATA = [
    {
        "difficulty": "easy",
        "text": "Which day is celebrated as republic day in india",
        "choices": ["15 august", "26 january", "2 october", "14 november"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "What is the capital city of France?",
        "choices": ["London", "Berlin", "Madrid", "Paris"],
        "correct": 3
    },
    {
        "difficulty": "easy",
        "text": "Which is the largest mammal on Earth?",
        "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "What is the chemical symbol for Water?",
        "choices": ["O2", "CO2", "H2O", "NaCl"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "Who wrote the play 'Romeo and Juliet'?",
        "choices": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which organ in the human body pumps blood?",
        "choices": ["Lungs", "Brain", "Liver", "Heart"],
        "correct": 3
    },
    {
        "difficulty": "easy",
        "text": "What is the boiling point of water at sea level?",
        "choices": ["90 degrees C", "100 degrees C", "110 degrees C", "120 degrees C"],
        "correct": 1
    },
    {
        "difficulty": "easy",
        "text": "Which is the smallest country in the world?",
        "choices": ["Monaco", "Maldives", "Vatican City", "San Marino"],
        "correct": 2
    },
    {
        "difficulty": "easy",
        "text": "Who is known as the 'Iron Man of India'?",
        "choices": ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhas Chandra Bose"],
        "correct": 1
    }
]


class Command(BaseCommand):
    help = 'Seed the database with initial quiz questions and choices'

    def handle(self, *args, **kwargs):
        created_q=0
        for item in DATA:
            q,created = Question.objects.get_or_create(
                text=item['text'],
                difficulty=item['difficulty']
                )
            if created:
                created_q += 1
            if q.choices.count() == 0:  # Only create choices if they don't already exist for this question    
               for idx, choice_text in enumerate(item['choices']):
                    is_correct = (idx == item['correct'])
                    Choice.objects.create(
                      question=q,
                      text=choice_text,
                      is_correct=is_correct
                    )
        self.stdout.write(self.style.SUCCESS(f"seeding completd - {created_q} questions added"))