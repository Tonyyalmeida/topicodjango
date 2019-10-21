
import datetime
import json
from django.http import HttpResponse

from django.test import TestCase
from django.utils import timezone


from .models import Question
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .apiviews import QuestionList

#class QuestionModelTests(TestCase):

 #   def test_was_published_recently_with_future_question(self):
  #      """
   #     was_published_recently() returns False for questions whose pub_date
    #    is in the future.
     #   """
      #  time = timezone.now() + datetime.timedelta(days=30)
       # future_question = Question(pub_date=time)
        #self.assertIs(future_question.was_published_recently(), False)


from rest_framework.test import APIClient

# ...


class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = QuestionList.as_view()
        self.uri = '/test/questions/'

    # ...
    def test_list2(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
        print(json.loads(response.content))
       # self.assertEqual(json.loads(response.content), {'id': 1, 'question_text': 'Where do you live?'})