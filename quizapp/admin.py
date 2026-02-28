from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Choice
from .models import QuizAttempt
from .models import AttemptAnswer   
from .models import AISettings


admin.site.register(Choice)
admin.site.register(QuizAttempt)
admin.site.register(AttemptAnswer)
admin.site.register(AISettings)

admin.site.register(Question)
