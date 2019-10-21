from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Question, Choice

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def landing(request):
    return HttpResponse("This is  the landing page")

def question_list(request):
    MAX_OBJECTS = 10
    questions = Question.objects.all()[:MAX_OBJECTS]
    data = {"results": list(questions.values("question_text", "id", "choice_text"))}
    return JsonResponse(data)

#def question_detail(request, pk):
#    details = get_object_or_404(Question, pk = pk)
 #   data = {"results": {
  #      "question": details.question_text,
   #     "id": details.id,
    #    "pub_date": details.pub_date
   # }}
   # return JsonResponse(data)

#""" # passing a URL parameter
#def detail(request, question_id):
#   return HttpResponse("You're looking at question %s." % question_id)

# """
# Create your views here