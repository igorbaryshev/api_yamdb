## Overview
**<span style="color:red">Ya</span>MDb API** is a Web API based on Django REST framework.
It allows people and third-party applications to connect to a database of reviews and information about media of different categories
such as films, music, books and many others.

When you run the project you'll be able to access various endpoints to enable usage of website functionality such as:
* adding and looking up information on titles, genres and categories
* reviewing titles
* commenting reviews
* editing user profiles as admin or own profile as authenticated user

The list of all available API endpoints can be accessed at `/redoc/` after running the project.

## Requirements
   * Python 3.7+
   * Django REST Framework 5.1.0+

## How to run:

#### 1. Clone the repository and open project directory using command-line:

    git clone https://github.com/igoralebar/api_yamdb.git
    cd api_yamdb

#### 2. Create and activate a virtual environment:
   
   * GNU/Linux or Mac:

       ```
       python3 -m venv venv
       ```
       ```
       source venv/bin/activate
       ```
   * Windows:
       ```
       python -m venv venv
       ```
       ```
       source venv/Scripts/activate
       ```

#### 3. Install all necessary dependencies from `requirements.txt`:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

#### 4. Apply migrations:

    python manage.py migrate

#### 5. Run the project:

    python manage.py runserver

#### All done! You can proceed to use the project.

### API request examples:
* Create a new title as admin `/api/v1/titles/`:
    ```json
    {
      "name": "Titanic",
      "year": 1997,
      "description": "A seventeen-year-old aristocrat falls in love...",
      "genre": [
        "drama",
        "romance"
      ],
      "category": "movie"
    }
    ```
* Get a list of titles of specific genre and category:
<br>
 `/api/v1/titles/?genre={genre_slug}&category={category_slug}`
<br>
<br>
* Create a new review as authenticated user`/api/v1/titles/{title_id}/reviews/`:
    ```json
    {
      "text": "string"
    }
    ```
* Create a new comment as authenticated user `/api/v1/titles/{title_id}/reviews/{review_id}/comments/`:
    ```json
    {
      "following": "string"
    }
    ```

* Sign up a new user or get confirmation code via email for existing one `/api/v1/auth/signup/`:
    ```json
    {
      "username": "my_username",
      "email": "my_email@example.com"
    }
    ```
* Get authentication token after providing confirmation code `/api/v1/auth/token/`:
    ```json
    {
      "username": "me_username",
      "confirmation_code": "ab1234-cdefghi567890jklmnopqrstuvwxyz123"
    }
    ```
