# User REST API

----
This API is used to manage the user lifecycle. It allows us to:

* Retrieve both a list of registered users, or a single user
* Register a user
* Update user information
* Delete a user  

----
**URL:**

_/users_

----
**Methods:**
  
`GET` | `POST` | `DELETE` | `PUT`

----  
**URL Params:**

| URL           |     Method    | Description                                |
| :---          |     :----:    | :---                                       |
| _/users/_     |     `GET`     | Retrieves ALL users from the database      |
| _/users/_     |     `POST`    | Adds a user to the database                |
| _/users/[id]_ |     `GET`     | Retrieves a single user from the database  |
| _/users/[id]_ |     `PUT`     | Updates an existing users details          |
| _/users/[id]_ |     `DELETE`  | Deletes an existing user from the database |

----
   **Required:**

   `id=[integer]`

----
**Data Params:**

  |         Key          |     Data Type    |        Description          |
  | :----                 |     :----:       | :---                        |
  |     username         |      String      |  The users username         |
  |     email            |      String      |  Email address of the user  |

  **_More to come!_**

----
**Success Response:**
  
  <_What should the status code be on success and is there any returned data? This is useful when people need to to know what their callbacks should expect!_>

* **Code:** 200 OK<br />
    **Content:** <br />
    ```

{
  "url": "http://127.0.0.1:8000/users/1/",
  "username": "foo",
  "email": "foo@bar.com",
  "groups": []`
}
    ```

**_More to come_**

----
**Error Response:**

* **Code:** 403 FORBIDDEN <br />
    **Content:** `{ detail: "Authentication credentials were not provided." }`

  OR

* **Code:** 400 BAD REQUEST <br />
    **Content:** `{ "username": ["A user with that username already exists."] }`

  OR

* **Code:** 400 BAD REQUEST <br />
    **Content:** `{ "username": ["This field may not be blank."] }`

----
**Sample Call:**

_Still to do_

**Notes:**

* Still to do:
    * Need to workout how to make sure it checks that no duplicate emails are added
    * Need to make email required field
    * Need to update fields when I know what all of them are
    * Update markdown to include any user creation into a default group so they only have certain priviledges
