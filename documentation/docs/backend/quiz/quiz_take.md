# Quiz Take App

## Overview and Motivation

The quiz_take app provides backend endpoints for the frontend to access using a REST API.

## Endpoints

All API endpoints have the root URL `/api/take-quiz/`; i.e. when a certain endpoint is stated to be located at `endpoint/location/`, it is actually located at `/api/take-quiz/endpoint/location/` or, more fully, `localhost:8081/api/take-quiz/endpoint/location/` where `localhost:8081` is where the Django backend is being hosted. Django's [captured value notation](https://docs.djangoproject.com/en/4.0/topics/http/urls/#example) is used in these docs. `pk` is an abbreviation for "primary key", which is essentially an ID assigned to objects stored in the database.

### Question Detail

Located at `question/<int:question_pk>/`. Provides support for GET requests to fetch the details of a specific question.

### Answers List

Located at `question/<int:question_pk>/answers/`. Provides support for GET requests to fetch a list of Answers associated with a specific question.

### Answer Detail

Located at `question/<int:question_pk>/answers/<int:answer_pk>/`. Provides support for GET requests to fetch the details of a specific Answer associated with a specific question.

### Topics List

Located at `question/<int:question_pk>/topics/`. Provides support for GET requests to fetch a list of Topics associated with a specific question.

### Topic Detail

Located at `question/<int:question_pk>/topics/<int:topic_pk>/`. Provides support for GET requests to fetch the details of a specific Topic associated with a specific question.

### Subject Detail

Located at `question/<int:question_pk>/subject/`. Provides support for GET requests to fetch the details of the subject that a specific question belongs to.

### Question Response Create

Located at `submit/question_response/`. Provides support for POST requests to create a QuestionResponse. Included in this response will be details such as the User submitting it, the question to which they are responding, and their selected Answer (all of which will be passed as primary keys referencing an object in the database). This endpoint should be used whenever a user submits a question (or more specifically, once they have submitted it such that they cannot change their response; depending on the frontend implementation, this may mean that many QuestionResponses are submitted at the end of a quiz [if the user can go back and change answers to previous questions while doing the quiz], or that one QuestionResponse is submitted whenever they answer a question [if the user cannot go back and change their answers while doing the quiz]).

### Quiz Statistics Create

Located at `submit/quiz_statistics/`. Provides support for POST requests to create a [QuizStatistics](./shared_models.md) object. This endpoint should be used when a user has completed a quiz, to send details about the quiz they just completed to the database (for later use on their user dashboard).

## Testing

Unit tests can be run from within the backend Docker container using the command `python manage.py test` (more verbosely if executing from a terminal not SSH'd into the container: `docker exec -it elucidate_server python manage.py test`). Ensure you are executing the command from the same directory as `manage.py`.
