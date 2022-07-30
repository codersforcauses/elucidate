# Shared Models App

## Overview and Motivation

The `shared_models` app is designed to hold the models and serializers that need to be used across multiple apps. This is to allow them to all access the same underlying models that don't belong to a single app, rather than having their own versions of these models and accessing each other's at random.

## Models

### Quiz

There are four shared quiz models:

* Question - a model representing a generic quiz question. Questions come in three types (represented by the `question_type` field): multiple choice, numerical answer and short answer. Each question has a numeric `marks` field, used to weight the question compared to others and give an estimation of its complexity/difficulty. There is also an `is_verified` field, which has a default value of False. Whenever a user submits a question, it will thus be unverified and will not appear in question pools when generating quizzes. Admins can access the admin dashboard and filter questions by their `is_verified` status, and manually approve (and modify if necessary) submitted questions.
* Subject - a model representing an ATAR subject and unit (e.g., Methods Unit 3, Chemistry Unit 1, Specialist Unit 4, Physics Unit 2, etc.). Each Question will have exactly one subject attached to it. subjects can be created, modified and deleted by admins only.
* Topic - a model representing a specific topic of a given subject (e.g., the subject "Methods Unit 3" might have the Topics "Differentiation", "Integration", "Logarithms", etc.). Each Topic is associated to a subject and the Topics for each subject will be different (e.g., the subject "English Unit 1" may have the Topics "Poetry", "Creative Writing" and "Prose", whereas the subject "Chemistry Unit 3" may have the topics "Redox Reactions", "Proteins" and "Equilibrium"). Each Question may have zero, one or many Topics attached to it. Topics will be able to be created and modified by admins for regular users to use to tag their Questions.
* Answer - a model representing an answer associated with a particular Question. Each Question can have multiple associated answers. Each answer can be marked as being correct or incorrect. For the three different types of Question, the intended use of the Answer model varies:
    * For multiple choice questions, each answer will appear as an option for the user taking the quiz to select. One or more answers will be correct, and the remaining answers will be incorrect.
    * For numerical answer questions, no options will be displayed, and the user must enter a numerical value into a text field. Each of the answers associated with such a Question should have `is_correct = True`, and if the user's input matches any of these answers, they will be marked correct. Answers which have `is_correct = False` will not do anything and hence **should not be added** to numerical answer questions.
    * For short answer questions, the user will be given an extended text field to enter their answer into. Due to the nature of this question, automated marking is not possible, and so the user will have to self-mark their response. Upon submitting their answer, all answers associated to the Question with `is_correct = True` will be displayed for the user to compare their response to. As with numerical answer questions, answers with `is_correct = False` will not do anything and hence **should not be added**.

### Statistics

* QuestionResponse - a model representing a response to a Question submitted by a User, stored in the database for statistics purposes. It stores the User that submitted the response, the Question they attempted, the answer they selected, and the date and time at which they submitted the response. This model is used for calculating properties in other statistics models. It also essentially constitutes the raw data of the system, so can be in principle extracted for deeper statistical analysis.
* UserStatistics - a model representing various statistics concerning a specific User, to be displayed on their user dashboard. Includes the number of quizzes they have completed, the number of questions the User has created, and their average score (over all the questions they have ever answered).
* QuizStatistics - a model representing various data relating to a quiz taken by a specific User, to be displayed on their user dashboard. Includes the quiz title, subject, topics, date taken, and score achieved for the quiz. Here, "quiz" refers to an ad-hoc quiz created by a user for revision purposes.
* QuestionStatistics - a model representing various statistics concerning a specific Question, for admin perusal. Includes a reference to the Question at hand, the total number of users who have attempted the question, and the average score (across all users who have attempted) for the question.
* TopicStatistics - a model representing various statistics concerning all questions falling under a specific Topic, for admin perusal. Includes a reference to the Topic at hand, and the average score (across all the attempts at all the questions under this topic) for the topic.

## Serializers

The `shared_models` app provides primary key serializers (`ModelSerializer`s) for each of the above models. The serializers provide `create` methods where necessary.

## Testing

Unit tests can be run from within the backend Docker container using the command `python manage.py test` (more verbosely if executing from a terminal not SSH'd into the container: `docker exec -it elucidate_server python manage.py test`). Ensure you are executing the command from the same directory as `manage.py`.
