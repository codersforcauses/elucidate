# Question Creation

## REST api

### Creating a question

- `quiz-api/question/`
    - GET - Returns an array of all the questions in the database
        - id
            - integer
            - database ID of the question
        - question_type
            - string
            - Can be either:
                - MC - Multiple Choice
                - NA - Numerical Answer
                - SA - Short Answer
                - See shared models app documentation for more info
        - text
            - string
            - question text
        - date_created
            - datetime
            - date and time that the quiz was created
    - POST - Add a question to the database
        - Required JSON fields:
            - question_type
                - string
                - Can be either:
                    - MC - Multiple Choice
                    - NA - Numerical Answer
                    - SA - Short Answer
                    - See shared models app documentation for more info
            - text
                - string
                - question text
            - date_created
                - datetime
                - date and time that the quiz was created
            - tags
                - string array
                - array of question tags
            - answers
                - 2D array
                - Can be empty or not included depending on the question type
                - An array of answer text and is_correct arrays, must be in the order: 1. answer text, 2. is_correct
                - e.g. "answers": [["Answer 1", true], ["Answer 2", false]]
                    - adds 2 answers, where answer 1 is correct while answer 2 is incorrect
                - invalid request: "answers": [[true, "Answer 1"], [false, "Answer 2"]]
                    - Invalid as answer text must be first, then if it's correct second

- `quiz-api/question/(question_id)/`
    - GET - Returns the question with the id `question_id`
    - PUT - update a question's text, question type, or date created. Can update only one or all 3 feields at a time
    - DELETE - Deletes the question and it's answers from the database

- `quiz-api/question/(question_id)/answer/`
    - GET - Returns an array of `question_id`s answers
        - id
            - integer
            - database ID of the answer
        - is_correct
            - boolean
            - is the answer correct
        - text
            - string
            - answer text
    - POST - Add an answer to `question_id`s question
        - Required JSON fields:
            - is_correct
                - boolean
                - is the answer correct
            - text
                - string
                - answer text
- `quiz-api/question/(question_id)/answer/(answer_id)`
    - GET - Returns a specific answer with the id `answer_id` from the question `question_id`
    - PUT - update an answer's text or is_correct. Can update only one or both feields at a time
    - DELETE - Removes the answer from the question and deletes it from the database

- `quiz-api/question/(question_id)/tag`
    - GET - Returns an array of `question_id`s tags
        - id
            - integer
            - database ID of the tag
        - name
            - string
            - tag text
    - POST - Add a tag to `question_id`s question
        - Required JSON fields:
            - name
                - string
                - tag text

- `quiz-api/question/(question_id)/answer/(answer_id)`
    - GET - Returns a specific tag with the id `answer_id` from the question `question_id`
    - DELETE - Removes the tag from the question but does not delete it from the database