# FitGirlsTracker API

## Description
This is a fitness tracking API built with Django and Django REST Framework. It provides endpoints for user authentication, managing user and expert profiles, tracking workout plans, and logging user activities. The API allows users to interact with fitness content, and it enables experts to manage and publish workout plans.

## Features
* **User Management:** Secure user registration, authentication, and profile management.
* **Expert Profiles:** Dedicated profiles for fitness experts with specific permissions.
* **Workout Plans:** Management of workout plans with details like name and difficulty.
* **User Activities:** Log and retrieve a history of a user's completed workouts and progress.
* **Social Interactions:** Users can like and comment on workout plans.
* **Token-Based Authentication:** All protected endpoints are secured using DRF's Token Authentication.

## Getting Started

### Prerequisites
* Python 3.13+
* Django and Django REST Framework
* A database (SQLite is configured by default)

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/fitgirlstracker_api.git](https://github.com/your-username/fitgirlstracker_api.git)
    cd fitgirlstracker_api
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```
6.  Start the development server:
    ```bash
    python manage.py runserver
    ```
The API will be available at http://127.0.0.1:8000/.

## API Endpoints

### Authentication
A user must first log in to receive an authentication token for accessing protected endpoints.

* **POST** `/auth/token/login/`
    * **Description:** Authenticates a user and returns an authentication token.
    * **Permissions:** `AllowAny`
    * **Body:**
        ```json
        {"username": "your-username", "password": "your-password"}
        ```

### User Management
* **POST** `/api/users/`
    * **Description:** Creates a new user account.
    * **Permissions:** `AllowAny`

### Workouts
* **GET** `/api/workouts/`
    * **Description:** Retrieves a list of all available workout plans.
    * **Permissions:** `IsAuthenticated`
* **POST** `/api/workouts/`
    * **Description:** Creates a new workout plan.
    * **Permissions:** `IsAuthenticated`, `IsExpert`
    * **Body:**
        ```json
        {"name": "New Workout", "difficulty": "Medium"}
        ```
* **GET** `/api/workouts/{id}/`
    * **Description:** Retrieves a specific workout plan by ID.
    * **Permissions:** `IsAuthenticated`
* **POST** `/api/workouts/{id}/like/`
    * **Description:** Likes or unlikes a workout.
    * **Permissions:** `IsAuthenticated`
* **GET** `/api/workouts/{id}/comments/`
    * **Description:** Retrieves comments for a specific workout.
    * **Permissions:** `IsAuthenticated`
* **POST** `/api/workouts/{id}/comments/`
    * **Description:** Adds a new comment to a specific workout.
    * **Permissions:** `IsAuthenticated`
    * **Body:**
        ```json
        {"text": "This is a great workout!"}
        ```

### User Activities
* **GET** `/api/user-activities/`
    * **Description:** Retrieves a list of the authenticated user's workout activities.
    * **Permissions:** `IsAuthenticated`
* **POST** `/api/user-activities/`
    * **Description:** Logs a new workout activity for the authenticated user.
    * **Permissions:** `IsAuthenticated`
    * **Body:**
        ```json
        {"workout": 1, "notes": "Completed my first run.", "date": "2025-08-29"}
        ```
* **GET** `/api/user-activities/history/`
    * **Description:** Retrieves a detailed history of the user's workout activities.
    * **Permissions:** `IsAuthenticated`