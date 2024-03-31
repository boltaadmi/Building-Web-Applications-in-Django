# Assuming you have already defined the models Question and Choice in your Django app

from django.contrib import admin
from django.urls import path

# Your models
from your_app_name.models import Question, Choice

# Define your admin classes
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# Register your models with the admin site
admin.site.register(Question, QuestionAdmin)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Now, in your Django shell:
from your_app_name.models import Question, Choice

# Insert a new question with the exact text
question_text = "Insert your question text here"
question = Question.objects.create(question_text=question_text)

# Create choices and associate them with the question
Choice.objects.create(question=question, choice_text="Choice 1")
Choice.objects.create(question=question, choice_text="Choice 2")
Choice.objects.create(question=question, choice_text="42")

# Verify the choices associated with the question
question.choice_set.all()
