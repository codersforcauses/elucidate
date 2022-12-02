# TODO: FIX TEST
# from datetime import datetime
# from django.contrib.auth import get_user_model
# from django.test import Client, TestCase

# from api.apps.shared_models.models.quiz_models import Subject


# class CreateQuizTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = get_user_model().objects.create_user(
#             "test@test.com",
#             "password",
#             grade="12",
#             first_name="John",
#             last_name="Smith",
#         )
#         self.client.login(email="test@test.com", password="password")

#         Subject.objects.create(name="Chemistry Unit 3")

#     def test_details(self):
#         response = self.client.post(
#             "/api/create-quiz/question/",
#             {
#                 "question_type": "SA",
#                 "text": "Test Question 1",
#                 "date_created": datetime.now(),
#                 "tags": ["tag1", "tag2"],
#                 "marks": 3,
#                 "subject": "Math",
#                 "answers": ["Example answer"],
#             },
#         )

#         json = response.json()
#         print(json)
#         self.assertEqual(json["question_type"], "SA")
#         self.assertEqual(json["text"], "Test Question 1")
#         question_id = json["id"]

#         response = self.client.get("/quiz-api/question/")
#         json = response.json()
#         self.assertEqual(json[0]["text"], "Test Question 1")

#         response = self.client.get(f"/quiz-api/question/{question_id}/")
#         json = response.json()
#         self.assertEqual(json["question_type"], "SA")
#         self.assertEqual(json["text"], "Test Question 1")

#         response = self.client.put(
#             f"/api/create-quiz/question/{question_id}/",
#             {"question_type": "MC"},
#             content_type="application/json",
#         )
#         json = response.json()
#         self.assertEqual(json["question_type"], "MC")

#         response = self.client.post(
#             f"/api/create-quiz/question/{question_id}/answer/",
#             {"is_correct": True, "text": "Test Answer 2"},
#         )
#         json = response.json()
#         self.assertEqual(json["is_correct"], True)
#         self.assertEqual(json["text"], "Test Answer 2")
#         answer_id = json["id"]

#         response = self.client.get(
#           f"/quiz-api/question/{question_id}/answer/")
#         json = response.json
#         self.assertEqual(json[0]["is_correct"], True)
#         self.assertEqual(json[0]["text"], "Test Answer 2")

#         response = self.client.get(
#             f"/api/create-quiz/question/{question_id}/answer/{answer_id}"
#         )
#         json = response.json()
#         self.assertEqual(json["is_correct"], True)
#         self.assertEqual(json["text"], "Test Answer 2")

#         response = self.client.put(
#             f"/api/create-quiz/question/{question_id}/answer/{answer_id}",
#             {"is_correct": False},
#             content_type="application/json",
#         )
#         json = response.json()
#         self.assertEqual(json["is_correct"], False)

#         response = self.client.post(
#             f"/api/create-quiz/question/{question_id}/tag/", {"name": "tag3"}
#         )
#         json = response.json()
#         self.assertEqual(json["name"], "tag3")
#         tag_id = json["id"]

#         response = self.client.get(f"/quiz-api/question/{question_id}/tag/")
#         json = response.json()
#         self.assertEqual(json[2]["name"], "tag3")

#         response = self.client.get(
#             f"/api/create-quiz/question/{question_id}/tag/{tag_id}"
#         )
#         json = response.json()
#         self.assertEqual(json["name"], "tag3")
