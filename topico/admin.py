from django.contrib import admin

# Register your models here.
from .models import Question, Choice, WordList, WordPair

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class WordPairInline(admin.TabularInline):
    model = WordPair
    extra = 2


class WordPairAdmin(admin.ModelAdmin):
#    fields = ['wordEnglish']
    list_display = ('wordEnglish', 'wordVietnamese', 'score')
  #  fields = ['wordEnglish', 'wordVietnamese'] 
    #'was_published_recently']
    # readonly_fields = ['was_published_recently'] 
# or "tabularinlie" vs ChoiceInline



class WordListAdmin(admin.ModelAdmin):
    fields = ['title', 'isTodo', 'user'] 
    #'was_published_recently']
    # readonly_fields = ['was_published_recently']
    inlines = [WordPairInline]   
# or "tabularinlie" vs ChoiceInline
    list_display = ('title', 'created', 'updated', 'isTodo', 'user')
    list_filter = ['isTodo']

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text'] 
    #'was_published_recently']
    # readonly_fields = ['was_published_recently']
    inlines = [ChoiceInline]   
# or "tabularinlie" vs ChoiceInline
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(WordPair, WordPairAdmin)
admin.site.register(WordList, WordListAdmin)
