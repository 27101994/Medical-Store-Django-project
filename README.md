# Medical Store Management System

## Requirements

- **Python Version:** 3.8.10
- **Database:** MySQL

## Installation

1. **Install virtualenvwrapper-win:**

   ```bash
   pip3 install virtualenvwrapper-win


2. Create a new virtual environment:

   ```bash
   mkvirtualenv your_project_env
   

3. Activate the virtual environment:

   ```bash
   workon your_project_env
   

4. Install Django inside the virtual environment:

   ```bash
   pip3 install django
   

5. Install project dependencies:

   ```bash
   pip3 install -r requirements.txt
   

## Database Setup

1. *Create a MySQL Database:*

   bash
   # Log in to MySQL with your credentials

   # Create a new database
   

2. *Update Django Settings:*

   Update the DATABASES configuration in your Django project's settings.py file with your MySQL database credentials.

## Database Migrations:

To create and apply database migrations:

1. Apply migrations to create the database arrangements:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   

## Run server

Run the development server:

   ```bash
   python manage.py runserver



## API Endpoints

- *signup*

  - Endpoint: http://127.0.0.1:8000/productsapi/signup
  - Method: POST
  - Body:
    json
    {
        "username": "username",
        "password1": "password",
        "password1": "conform_password",
    }

- *login*

  - Endpoint: http://127.0.0.1:8000/productsapi/login
  - Method: POST
  - Body:
    json
    {
        "username": "username",
        "password1": "password",
    } 
  - Response: Token_is_generated 
    

- *create_product*

  - Endpoint: http://127.0.0.1:8000/productsapi/create_product
  - Method: POST
  - Headers:  
    Authorization:Token your_generated_token_here
  - Body:
    json
    {
        "name": "medicine_name",
        "description": "medicine_description",
        "price": "medicine_price",
    }  


- *update_productr*

  - Endpoint: http://127.0.0.1:8000/productsapi/<product_id>/update_product
  - Method: PUT
  - Headers:  
    Authorization:Token your_generated_token_here
  - Body:
    json
    {
        "name": "medicine_name",
        "description": "medicine_description",
        "price": "medicine_price",
    } 

- *list_products*

  - Endpoint: http://127.0.0.1:8000/productsapi/list_products
  - Method: GET
  - Headers:  
    Authorization:Token your_generated_token_here
    

- *delete_product*

  - Endpoint: http://127.0.0.1:8000/productsapi/<product_id>/delete_product
  - Method: DELETE
  - Headers:  
    Authorization:Token your_generated_token_here

- *search*
  - Endpoint: http://127.0.0.1:8000/productsapi/search
  - Method: GET
  - Headers:  
    Authorization:Token your_generated_token_here

