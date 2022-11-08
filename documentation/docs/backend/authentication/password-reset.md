# Authentication REST API

----
This API is used to manage the password reset lifecycle. It allows us to:

* Send a password reset email with an SMTP server (currently configured for gmail)
* Verfiy that a token and associated uid is valid
* Reset the user password using a valid token and associated uid

----
**Base URL:**

/api/auth/reset

----  

**Endpoints:**

## /

Methods: POST, PUT
Description: PUT to veriy that a token/uid pair is valid. POST to change passwords.

**URL Parameters**

  | Key   | Data Type | Description                                            |
  | :---- | :-------: | :----------------------------------------------------- |
  | token |  String   | A password reset token.                                |
  | uid   |  String   | The url-safe base64 encoded email address of the user. |

**Data Parameters:**

  | Key      | Data Type | Description       |
  | :------- | :-------: | :---------------- |
  | password |  String   | The new password. |

Example request

```json
{
    "password": "123456",
}
```

Example response

```json
// TODO
```

## /email/

Methods: POST
Description: Register an user. Returns the user JSON as the response.
Success status code: 200 OK

**Data Parameters:**

  | Key   | Data Type | Description            |
  | :---- | :-------: | :--------------------- |
  | email |  String   | The email of the user. |
