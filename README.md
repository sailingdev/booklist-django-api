# Book-list

Book list REST API written with Django Rest Framework

# Goal

Create a Django API using Django Rest Framework that lists a filterable list of books. Books must store writer, name, synopsis, genre, release date, price in cents. The list API must be paginated, searchable and filterable by multiple genres.

# Database migration

    python manage.py makemigrations
    python manage.py migrate

# Run

    python manage.py runserver

Then you will be seeing the application running on localhost:8000.
