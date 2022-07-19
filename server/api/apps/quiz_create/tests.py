from django.test import TestCase, Client
from datetime import datetime
import json


def ByteToJSON(JSONBytes):
    return json.loads(JSONBytes.decode('utf-8'))


class CreateQuizTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.post(
            '/quiz-api/question/',
            {
                'question_type': 0,
                'question': 'Test Question 1',
                'date_created': datetime.now(),
                'tags': ['tag1', 'tag2']})
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 0)
        self.assertEqual(json['question'], 'Test Question 1')
        question_id = json['id']

        response = self.client.get('/quiz-api/question/')
        json = ByteToJSON(response.content)
        self.assertEqual(json[0]['question'], 'Test Question 1')

        response = self.client.get(F'/quiz-api/question/{question_id}/')
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 0)
        self.assertEqual(json['question'], 'Test Question 1')

        response = self.client.put(
            F'/quiz-api/question/{question_id}/',
            {'question_type': 2},
            content_type='application/json'
        )
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 2)

        response = self.client.post(
            F'/quiz-api/question/{question_id}/answer/',
            {'is_correct': True, 'answer': 'Test Answer 1'})
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], True)
        self.assertEqual(json['answer'], 'Test Answer 1')

        response = self.client.get(F'/quiz-api/question/{question_id}/answer/')
        json = ByteToJSON(response.content)
        self.assertEqual(json[0]['is_correct'], True)
        self.assertEqual(json[0]['answer'], 'Test Answer 1')
        answer_id = json[0]['id']

        response = self.client.get(
            F'/quiz-api/question/{question_id}/answer/{answer_id}')
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], True)
        self.assertEqual(json['answer'], 'Test Answer 1')

        response = self.client.put(
            F'/quiz-api/question/{question_id}/answer/{answer_id}',
            {'is_correct': False},
            content_type='application/json'
        )
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], False)

        response = self.client.post(
            F'/quiz-api/question/{question_id}/tag',
            {"tag": "tag3"})
        json = ByteToJSON(response.content)
        self.assertEqual(json['tag'], 'tag3')

        response = self.client.get(F'/quiz-api/question/{question_id}/tag')
        json = ByteToJSON(response.content)
        self.assertEqual(json[2]['tag'], 'tag3')
