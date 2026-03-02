from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import QuizAttempt
from .models import AttemptAnswer   
from .models import AISettings


# admin.site.register(Choice)
# admin.site.register(QuizAttempt)
# admin.site.register(AttemptAnswer)
# admin.site.register(AISettings)

# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4  # Number of extra choice fields to display when adding a new question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'difficulty',) # Display the text, difficulty, and creation date of each question in the admin list view
    search_fields = ('text',) # Enable search functionality for the question text in the admin interface
    list_filter = ('difficulty',) # Add a filter sidebar to filter questions by difficulty level in the admin interface
    inlines = [ChoiceInline] # Include the ChoiceInline to allow adding/editing choices directly from the Question admin page


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'difficulty', 'score', 'started_at', 'completed_at') # Display relevant fields of QuizAttempt in the admin list view
    search_fields = ('player_name',) # Enable search functionality for player names in the admin interface
    list_filter = ('difficulty','started_at','completed_at') # Add a filter sidebar to filter quiz attempts by difficulty level in the admin interface
    readonly_fields = ('started_at', 'completed_at','score','total_questions') # Make the started_at and completed_at fields read-only in the admin interface to prevent manual editing


@admin.register(AISettings)
class AISettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'gemini_model', 'updated_at') # Display relevant fields of AISettings in the admin list view
    readonly_fields = ('updated_at',) # Make the updated_at field read-only in the admin interface to prevent manual editing


@admin.register(AttemptAnswer)
class AttemptAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempt', 'question', 'order', 'selected_choice', 'is_correct','ai_explanation','ai_learn_more') # Display relevant fields of AttemptAnswer in the admin list view
    search_fields = ('attempt__player_name', 'question__text') # Enable search functionality for player names and question text in the admin interface
    list_filter = ('is_correct',) # Add a filter sidebar to filter attempt answers by correctness in the admin interface