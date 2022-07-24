# Shared Models App

## Overview and Motivation

The `shared_models` app is designed to hold the models and serializers that need to be used across multiple apps. This is to allow them to all access the same underlying models that don't belong to a single app, rather than having their own versions of these models and accessing each other's at random.

## Models

### Quiz

There are four shared quiz models:

* Question - a model representing a generic quiz question. Questions come in three types (represented by the `question_type` field): multiple choice, numerical answer and short answer.
* Topic - a model representing a specific subject topic. Topics can be attached to many Questions (and each Question may have many associated topics). topics will be able to be created and modified by admins for regular users to use to tag their questions.
* Subject - a model representing a school subject. There can be many topics for one subject. Subjects are not connected to questions, as it is simpler for the backend to derive the subjects from the topics instead of having both topics and subjects connected to a question which complicates things. Subjects can also be created and modified by admins.
* Answer - a model representing an answer associated with a particular Question. Each Question can have multiple associated answers. Each answer can be marked as being correct or incorrect. For the three different types of Question, the intended use of the Answer model varies:
  * For multiple choice questions, each Answer will appear as an option for the user taking the quiz to select. One or more Answers will be correct, and the remaining Answers will be incorrect.
  * For numerical answer questions, no options will be displayed, and the user must enter a numerical value into a text field. Each of the Answers associated with such a Question should have `is_correct = True`, and if the user's input matches any of these answers, they will be marked correct. Answers which have `is_correct = False` will not do anything and hence **should not be added** to numerical answer questions.
  * For short answer questions, the user will be given an extended text field to enter their answer into. Due to the nature of this question, automated marking is not possible, and so the user will have to self-mark their response. Upon submitting their answer, all Answers associated to the Question with `is_correct = True` will be displayed for the user to compare their response to. As with numerical answer questions, Answers with `is_correct = False` will not do anything and hence **should not be added**.

### Statistics

* QuizStatistics - a model representing a response to a Quiz submitted by a User, stored in the database for statistics purposes. The QuizStatistics model contains all of the necessary data for the following statistics to be surmised, as per the client's requirements:
  * How many questions the quiz has
  * Total marks and the user's mark
  * How long the User took to complete the Quiz
  * When the quiz was taken
  * How many Users in total have attempted a given Quiz
  * The average score (across all Users) for a given Question
  * The average score (across all Users) for a given Tag (i.e. subject and topic)

## Serializers

The `shared_models` app provides serializers for each of the above models.

## Testing

Unit tests can be run from within the backend Docker container using the command `python manage.py test` (more verbosely if executing from a terminal not SSH'd into the container: `docker exec -it elucidate_server python manage.py test`). Ensure you are executing the command from the same directory as `manage.py`.
