# Quiz Generation

## Overview and Motivation

The quiz_generation app provides backend endpoints for the frontend to generate quizzes based on subject, topics and question count, and also provides the ability to check if a subject or topic exists in the DB.

## Endpoints

All API endpoints have the root URL `/api/generate-quiz/`. `pk` is an abbreviation for "primary key", which is essentially an ID assigned to objects stored in the database.

### Generate Quizzes

Located at `/api/generate-quiz/generate`, provides support for POST requests. Use this to generate a quiz.

JSON fields:
    - `subject`
      - PK of a subject
    - `topics`
      - an array of topic PKs that must relate to the subject.
    - `question_count`
      - amount of questions that should be returned. If the amount is higher than the amount of verified questions with the subject and topics, then it will return all available questions.
    - Return JSON:
      - The method will return an array of randomised, verified question PKs with the field name `pk_array`.

### Check if a subject exists

Located at `/api/generate-quiz/subject-exists`, provides support for POST requests. It checks if a subject exists in the database, and returns its PK.

JSON fields:
    - `name`
      - name of the subject.
    - Return JSON:
      - The method will return the PK of the subject with the field name `pk`. It will return a 404 if the name isn't found in the database.

### Check if a topic exists

Located at `/api/generate-quiz/topic-exists`, provides support for POST requests. It checks if a topic exists in the database, and returns its PK.

JSON fields:
    - `name`
      - name of the topic.
    - `subject`
      - PK of the subject that the topic is related to.
    - Return JSON:
      - The method will return the PK of the topic with the field name `pk`. It will return a 404 if the name isn't found in the database or it isn't related to the subject.
