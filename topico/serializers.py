from rest_framework import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import MyUser, Question, Choice, Snippet, WordList, WordPair, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework.validators import UniqueValidator
#Vote

#class VoteSerializer(serializers.ModelSerializer): class Meta:
 #       model = Vote
  #      fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
 #   votes = VoteSerializer(many=True, required=False)
  #  votes = serializer.
    
    votes = serializers.IntegerField(max_value=10)
    class Meta:
        model = Choice
        #fields = "__all__"
        exclude = ['question']
   # def save(self, question):


class QuestionSerializer(serializers.ModelSerializer):
  #  Choice = '<>' #the extra attribute value
    choices  = ChoiceSerializer(many=True, required=False, read_only=True)
    class Meta: 
        model = Question
        fields = "__all__"

class QuestionListSerializer(serializers.ModelSerializer):
  #  Choice = '<>' #the extra attribute value
 #   choices  = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta: 
        model = Question
        fields = "__all__"

class WordPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordPair
        fields = "__all__"
        extra_kwargs = {'id': {
                'read_only': True, 
                'required': True,
             }}
        

class WordListListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordList
        fields = "__all__"

class WordListSerializer(serializers.ModelSerializer):
    WordPairs = WordPairSerializer(many=True, required=False)
    extra_kwargs = {'id': {
                'read_only': False, 
                'required': True
             }}
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.isTodo = validated_data.get("isTodo", instance.isTodo)
        instance.save()
        if "WordPairs" in validated_data:
            wordpairdata = validated_data.pop("WordPairs")
            for mydata in wordpairdata:
                ownerObj = get_object_or_404(WordPair, pk=mydata["id"])
                ownerObj.wordEnglish = mydata.get('wordEnglish',ownerObj.wordEnglish)
                ownerObj.wordVietnamese = mydata.get('wordVietnamese',ownerObj.wordVietnamese)
                ownerObj.exampleEnglish = mydata.get('exmapleEnglish',ownerObj.exampleEnglish)
                ownerObj.exampleVietnamese = mydata.get('exampleVietnamese',ownerObj.exampleVietnamese)
                ownerObj.score = mydata.get('score',ownerObj.score)
                ownerObj.save()
        return instance
    class Meta:
        model = WordList
        fields = "__all__"

#class WordPairSerializer(serializers.ModelSerializer):
 #   class Meta: 
  #      model = WordPair
   #     fields = "__all__"

#class WordListSerializer(serializers.ModelSerializer):
 #   class Meta: 
  #      model = WordList
   #     fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta: 
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data): 
      user = User(
          email=validated_data['email'],
          username=validated_data['username']
      )
      user.set_password(validated_data['password']) 
      user.save()
      return user

