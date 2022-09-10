# Authentication REST API

----
This API is used to manage the authentication lifecycle. It allows us to:

* Register a user
* Login by acquiring a JWT
* Verify that the JWT is valid
* Refresh the JWT
* [TODO] Log out a user  
* [TODO] Delete a user

----
**Base URL:**

/api/auth

----  

**Endpoints:**

## /register/

Methods: POST
Description: Register an user. Returns the user JSON as the response.
Success status code: 201 Created

**Data Parameters:**

  | Key        | Data Type | Description                                                    |
  | :--------- | :-------: | :------------------------------------------------------------- |
  | email      |  String   | Email address of the user                                      |
  | password   |  String   | Password of the user. Minimum 6 characters.                    |
  | first_name |  String   | First name of the user                                         |
  | last_name  |  String   | Last name of the user                                          |
  | grade      |  String   | Grade of the user, options are "Year 11", "Year 12" or "Other" |

Example request

```json
{
    "email": "john.doe@example.com",
    "password": "password",
    "first_name": "John",
    "last_name": "Doe",
    "grade": "Grade 11"
}
```

Example response

```json
{
    "email": "john.doe@example.com",
    "password": "password",
    "first_name": "John",
    "last_name": "Doe",
    "grade": "Grade 11"
}
```

## /login/

Methods: POST
Description: Login an user. Returns the access token as a JSON body.
Success status code: 201 Created

**Data Parameters:**

  | Key      | Data Type | Description                                 |
  | :------- | :-------: | :------------------------------------------ |
  | email    |  String   | Email address of the user                   |
  | password |  String   | Password of the user. Minimum 6 characters. |

Example request

```json
{
    "password": "",
    "email": ""
}
```

Example response

```json
{
    "pk": 1658233060,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFAYS5jb20iLCJpYXQiOjE2NTgyMzMwNjAsImV4cCI6MTY1ODgzNzg2MCwianRpIjoiMTYwMGNlODktNTc0Mi00ZWU3LWFlYmEtZGVhODJkZDQxNWYxIiwidXNlcl9pZCI6MTAsIm9yaWdfaWF0IjoxNjU4MjMzMDYwfQ.fHaRBcnwgbfJtx3TVcBKh0sDHcWd4qE4myB4E-BubCk"
}
```

## /verify/

Methods: POST
Description: Verifies if a token is valid and not expired. Returns the access token as a JSON body.
Success status code: 201 Created

**Data Parameters:**

  | Key   | Data Type | Description      |
  | :---- | :-------: | :--------------- |
  | token |  String   | The JWT to check |

Example request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFAYS5jb20iLCJpYXQiOjE2NTgyMzMwNjAsImV4cCI6MTY1ODgzNzg2MCwianRpIjoiMTYwMGNlODktNTc0Mi00ZWU3LWFlYmEtZGVhODJkZDQxNWYxIiwidXNlcl9pZCI6MTAsIm9yaWdfaWF0IjoxNjU4MjMzMDYwfQ.fHaRBcnwgbfJtx3TVcBKh0sDHcWd4qE4myB4E-BubCk"
}
```

Example response

```json
{
    "pk": 1658233060,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFAYS5jb20iLCJpYXQiOjE2NTgyMzMwNjAsImV4cCI6MTY1ODgzNzg2MCwianRpIjoiMTYwMGNlODktNTc0Mi00ZWU3LWFlYmEtZGVhODJkZDQxNWYxIiwidXNlcl9pZCI6MTAsIm9yaWdfaWF0IjoxNjU4MjMzMDYwfQ.fHaRBcnwgbfJtx3TVcBKh0sDHcWd4qE4myB4E-BubCk"
}
```

## /refresh/

Methods: POST
Description: Refreshes a JWT that is close to expiry. Returns a new access token as a JSON body.
Success status code: 201 Created

**Data Parameters:**

  | Key   | Data Type | Description        |
  | :---- | :-------: | :----------------- |
  | token |  String   | The JWT to refresh |

Example request

```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFAYS5jb20iLCJpYXQiOjE2NTgyMzMwNjAsImV4cCI6MTY1ODgzNzg2MCwianRpIjoiMTYwMGNlODktNTc0Mi00ZWU3LWFlYmEtZGVhODJkZDQxNWYxIiwidXNlcl9pZCI6MTAsIm9yaWdfaWF0IjoxNjU4MjMzMDYwfQ.fHaRBcnwgbfJtx3TVcBKh0sDHcWd4qE4myB4E-BubCk"
}
```

Example response

```json
{
    "pk": 1658236951,
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFAYS5jb20iLCJpYXQiOjE2NTgyMzY5NTEsImV4cCI6MTY1ODg0MTc1MSwianRpIjoiZDVmZDgzYjEtNTY0ZS00NjNjLTliOWQtYmY2ODIwOTIxMWQ3IiwidXNlcl9pZCI6MTAsIm9yaWdfaWF0IjoxNjU4MjMzMDYwLCJvcmlnX2p0aSI6IjE2MDBjZTg5LTU3NDItNGVlNy1hZWJhLWRlYTgyZGQ0MTVmMSJ9.pKzRkGeQCxrkqH-tyGMNg6TwLLoIhXwGv873CeFH_AU"
}
```
