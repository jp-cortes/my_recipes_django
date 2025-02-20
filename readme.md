My recipes
===========

Welcome to my recipes project! This Django application is designed to manage recipes, menus, and users efficiently.

Requirements
------------

*   **PostgreSQL** (Make sure it's installed and running)
*   **Python 3.11**

Installation Guide
------------------

Follow these steps to get the project up and running on your local machine.

### 1\. Clone the Repository

Clone the project repository from GitHub to your local machine.

```bash
git clone https://github.com/jp-cortes/my-recipes.git my_recipes
cd my_recipes
```

### 2\. Set Up Virtual Environment

Create and activate a virtual environment.


```bash
python3.11 -m venv venv 
source venv/bin/activate 
```

### 3\. Install Dependencies

Install the required Python packages using `pip`.

`pip install -r requirements.txt`

### 4\. Configure Environment Variables

Create a `.env` file in the root of the project. You can use `.env.example` as a template.


`cp .env.example .env`

Update the `.env` file with your database credentials and other necessary configurations.

### 5\. Set Up the Database

Create the PostgreSQL database and apply migrations.

```bash
psql -U postgres CREATE DATABASE coffeeshop;
```
Apply migrations 

```bash
python manage.py migrate
```

### 6\. Create a Superuser

Create a superuser to access the Django admin interface.


```
python manage.py createsuperuser
```

### 7\. Run the Development Server

Start the Django development server.

```
./manage.py runserver
```

Access the project by navigating to `http://127.0.0.1:8000` in your web browser.

Project Structure
-----------------

*   **recipes**: Handles everything related to recipes.
*   **users**: Manages user authentication and profiles.
*   **menus**: Manages user recipes.

Contributing
------------

We welcome contributions! Please fork the repository and submit pull requests for any features, improvements, or bug fixes.
