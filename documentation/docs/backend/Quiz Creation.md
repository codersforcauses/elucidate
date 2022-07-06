# Quiz Creation

## Quiz model structure

### Quiz_Tag class

- tag
    - The tag name
    - CharField type
    - Has a max length of 15

### Quiz_Objective class

- objective
    - The objective name
    - CharField type
    - Has a max length of 15

### Quiz_Details class

- name
    - The quiz name
    - CharField type
    - Has a max length of 100
- time_limit
    - The quiz time limit
    - PositiveIntegerField type
- date_created
    - Date that the quiz was made
    - DateTimeField type
    - Is set to the current time when first created
- creator
    - The user that created the quiz
    - Many to one relationship with the User class
- tags
    - The tags of the quiz
    - Many to many relationship with the Quiz_Tag class
- objectives
    - the objectives of the quiz
    - Many to many relationship with the Quiz_Objective class
- number_of_questions
    - Amount of questions in the quiz
    - PositiveIntegerField type
    - default is 1

### Quiz_Question class

- quiz
    - The quiz that the question is connected to
    - Many to one relationship with the Quiz_Details class
- is_multichoice
    - Is the question multichoice or short answer
    - BooleanField type
- question
    - The question text
    - CharField type
    - Has a max length of 100

### Question_Answer class
- question
    - The question that the answer is connected to
    - Many to one relationship with the Quiz_Question class
- is_correct
    - Is the question correct or not
    - BooleanField type
    - Not used if the question type is short answer, as it would only have one answer
- answer
    - The answer text
    - CharField type
    - Has a max length of 100
    - If the question type is multiple choice, multiple 'Question_Answer' objects would be created for each possible answer and the correct answer would have 'is_correct' set to true. If it is a short answer type, only one 'Question_Answer' object would be created and 'answer' would be set to the keywords. I'm still not 100% on this implementation, so if anyone knows a better way let backend know.