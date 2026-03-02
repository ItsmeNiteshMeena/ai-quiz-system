from django.db import models

# Create your models 

DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),     # Tuple of difficulty choices for the Question model, where the first element is the value stored in the database and the second element is the human-readable name displayed in forms.
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]


class Question(models.Model):
    text = models.CharField(max_length=200) # Field to store the text of the quiz question, with a maximum length of 200 characters.
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,default='medium')# Field to store the difficulty level of the question, using the predefined choices from DIFFICULTY_CHOICES, with a default value of 'medium'.
    created_at = models.DateTimeField(auto_now_add=True)# Field to automatically set the timestamp when a new question is created, using auto_now_add=True to ensure it is only set once at creation time.

    def __str__(self): # __str__ method to define the string representation of the Question model.
        return f"[{self.difficulty}] {self.text[:50]}..." # f-string to format the string representation of the question, showing the difficulty and the first 50 characters of the text.
    
class Choice(models.Model):     # Model to represent the answer choices for each quiz question, with a foreign key relationship to the Question model.
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices') # ForeignKey field to link each choice to a specific question, with on_delete=models.CASCADE to ensure that choices are deleted if the associated question is deleted, and related_name='choices' to allow reverse access from the Question model.
    text = models.CharField(max_length=100) # Field to store the text of the answer choice, with a maximum length of 100 characters.
    is_correct = models.BooleanField(default=False) # Boolean field to indicate whether the choice is the correct answer for the question, with a default value of False.

    def __str__(self):
        return self.text
    
class QuizAttempt(models.Model):
    player_name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES,default='medium') # Field to store the difficulty level of the quiz attempt, using the predefined choices from DIFFICULTY_CHOICES, with a default value of 'medium'.
    total_questions = models.PositiveIntegerField(default=10)
    score = models.PositiveIntegerField(default=0) # Field to store the player's score for the quiz attempt, with a default value of 0.
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_limit_seconds = models.PositiveIntegerField(default=300)  # Default time limit of 5 minutes
    expires_at = models.DateTimeField(null=True, blank=True)  # Optional field to set an expiration time for the quiz attempt
    def __str__(self):
        return f"Attempt for '{self.player_name} - {self.difficulty}'"    
    
class AttemptAnswer(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers') #
    question = models.ForeignKey(Question, on_delete=models.PROTECT) # Use PROTECT to prevent deletion of questions that have been answered in attempts
    order = models.PositiveIntegerField() # Field to track the order of questions in the quiz attempt 
    selected_choice = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True) # Use SET_NULL to allow for unanswered questions without deleting the AttemptAnswer record
    is_correct = models.BooleanField(null=True, blank=True) # Field to indicate whether the selected choice is correct or not
    ai_explanation = models.TextField(blank=True,default="") # Optional field to store AI-generated explanations for the answer
    ai_learn_more=models.TextField(blank=True,default="") # Optional field to store AI-generated "learn more" content related to the question or answer
    def __str__(self):
        return f"Attempt '{self.attempt.id}' - Q {self.order}"    
    
class AISettings(models.Model):
    gemini_api_key = models.TextField(blank=True,default="") # Field to store the Gemini API key for AI integration
    gemini_model = models.CharField(max_length=100, default='gemini-2.5-flash') # Field to specify the Gemini model to use for AI interactions, with a default value of 'gemini-2.0-pro'
    updated_at = models.DateTimeField(auto_now=True) # Field to automatically update the timestamp whenever the AI settings are modified
    def __str__(self):
        return f"AI Settings"

    @classmethod  
    def get_solo(cls):
        obj,_ = AISettings.objects.get_or_create(id=1) # Class method to retrieve the singleton instance of AISettings, creating it if it doesn't exist
        return obj