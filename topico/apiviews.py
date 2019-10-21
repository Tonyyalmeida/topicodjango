from rest_framework import generics
from .models import Question, Choice, WordList, WordPair
from .serializers import QuestionSerializer, ChoiceSerializer, QuestionListSerializer, UserSerializer, WordListListsSerializer, WordListSerializer, WordPairSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend, BooleanFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


#class QuestionList(generics.ListCreateAPIView): 
 #   queryset = Question.objects.all() 
  #  serializer_class = QuestionSerializer
#class QuestionDetail(generics.RetrieveDestroyAPIView): 
 #   queryset = Question.objects.all()
  #  serializer_class = QuestionSerializer

#class QuestionList(APIView): 
#also works - what is the difference?
#class QuestionList(generics.ListAPIView)
#    def get(self, request):
 #       questions = Question.objects.all()[:20]
  #      data = QuestionListSerializer(questions, many=True).data 
     #   return Response(data)

class QuestionList(generics.ListCreateAPIView): 
    queryset = Question.objects.all() 
    serializer_class = QuestionListSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
#viewsets.ModelViewSet
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
#API to edit the questionxs
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
  #  def get(self, request, pk):
   #     question = get_object_or_404(Question, pk=pk) 
    #    data = QuestionSerializer(question).data 
     #   return Response(data)
class WordListListFilter(filters.FilterSet):
   # isTodo = BooleanFilter(name='isTodo')
    class Meta:
        model = WordList
        fields = ['id', 'created', 'isTodo', 'user']

class WordListList(generics.CreateAPIView, generics.ListAPIView): 
    queryset = WordList.objects.all() 
    serializer_class = WordListListsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = StandardResultsSetPagination
    #works well
    #filterset_fields = ['score', 'wordList']
    search_fields = ['title']
    filterset_class = WordListListFilter

class WordListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer

class WordPairFilter(filters.FilterSet):
    min_score = filters.NumberFilter(field_name="score", lookup_expr='gte')
    max_score = filters.NumberFilter(field_name="score", lookup_expr='lte')
    class Meta:
        model = WordPair
        fields = ['id', 'wordEnglish', 'wordVietnamese', 'score', 'wordList']
        
class WordPairCreation(generics.CreateAPIView, generics.ListAPIView):
    queryset = WordPair.objects.all()
    serializer_class = WordPairSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = StandardResultsSetPagination
    #works well
    #filterset_fields = ['score', 'wordList']
    search_fields = ['wordEnglish']
    filterset_class = WordPairFilter
    #works well


class WordPairDetail(generics.RetrieveUpdateAPIView):
    queryset = WordPair.objects.all()
    serializer_class = WordPairSerializer

class ChoiceList(generics.CreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer     
    lookup_url_kwarg = 'pk' 
    def perform_create(self, serializer):
        pk = self.kwargs['pko']
        serializer.save(question_id = pk)
#question_id is generated automatiicaly from model (it's called question there)


 #   def get_queryset(self):
  #      print("haallo")
   #     queryset = Choice.objects.filter(question_id=self.kwargs["question_id"])
   #     return queryset

def vote_view(request, question_pk, choice_pk):
  #URL variables can be accessed from here directly
#  serializer_class = ChoiceSerializer
#    print(request)
 #   question = get_object_or_404(Question, pk=question_id)
#  if serializer.is_valid():
  choice = get_object_or_404(Choice, pk=choice_pk)
  if choice.question_id == question_pk:
    choice.votes += 1
    choice.save()
    choice_data = ChoiceSerializer(choice)
    return JsonResponse({'choice': choice_data.data}, status=200)
  else: return JsonResponse({"error": 'Choice is not part of the question'}, status=400)
#    return Response(serializer.errors)

#class QuestionDetail(APIView):
 #   def get(self, request, pk):
  #      question = get_object_or_404(Question, pk=pk)
   #     data = QuestionSerializer(question).data 
    #    return Response(data)


class UserCreate(generics.CreateAPIView):
  authentication_classes = ()
  permission_classes = ()
  serializer_class = UserSerializer
