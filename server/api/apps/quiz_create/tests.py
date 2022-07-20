from django.test import TestCase, Client
from datetime import datetime
import json


def ByteToJSON(JSONBytes):
    try:
        return json.loads(JSONBytes.decode('utf-8'))
    except json.JSONDecodeError:
        raise Exception(JSONBytes)


class CreateQuizTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_details(self):
        response = self.client.post(
            '/quiz-api/question/',
            {
                'question_type': 'SA',
                'text': 'Test Question 1',
                'date_created': datetime.now(),
                'tags': ['tag1', 'tag2']})
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 'SA')
        self.assertEqual(json['text'], 'Test Question 1')
        question_id = json['id']

        response = self.client.get('/quiz-api/question/')
        json = ByteToJSON(response.content)
        self.assertEqual(json[0]['text'], 'Test Question 1')

        response = self.client.get(F'/quiz-api/question/{question_id}/')
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 'SA')
        self.assertEqual(json['text'], 'Test Question 1')

        response = self.client.put(
            F'/quiz-api/question/{question_id}/',
            {'question_type': 'MC'},
            content_type='application/json'
        )
        json = ByteToJSON(response.content)
        self.assertEqual(json['question_type'], 'MC')

        response = self.client.post(
            F'/quiz-api/question/{question_id}/answer/',
            {'is_correct': True, 'text': 'Test Answer 2'})
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], True)
        self.assertEqual(json['text'], 'Test Answer 2')
        answer_id = json['id']

        response = self.client.get(F'/quiz-api/question/{question_id}/answer/')
        json = ByteToJSON(response.content)
        self.assertEqual(json[0]['is_correct'], True)
        self.assertEqual(json[0]['text'], 'Test Answer 2')

        response = self.client.get(
            F'/quiz-api/question/{question_id}/answer/{answer_id}')
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], True)
        self.assertEqual(json['text'], 'Test Answer 2')

        response = self.client.put(
            F'/quiz-api/question/{question_id}/answer/{answer_id}',
            {'is_correct': False},
            content_type='application/json'
        )
        json = ByteToJSON(response.content)
        self.assertEqual(json['is_correct'], False)

        response = self.client.post(
            F'/quiz-api/question/{question_id}/tag/',
            {'name': 'tag3'})
        json = ByteToJSON(response.content)
        self.assertEqual(json['name'], 'tag3')
        tag_id = json['id']

        response = self.client.get(F'/quiz-api/question/{question_id}/tag/')
        json = ByteToJSON(response.content)
        self.assertEqual(json[2]['name'], 'tag3')

        response = self.client.get(
            F'/quiz-api/question/{question_id}/tag/{tag_id}')
        json = ByteToJSON(response.content)
        self.assertEqual(json['name'], 'tag3')
