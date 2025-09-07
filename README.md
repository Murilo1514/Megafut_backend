# How to run
    cd backend
    python manage.py runserver

# How to see the data
    sqlite3 db.sqlite3
    .tables;          -- list the tables
    .schema auth_user -- show the structure of table
    SELECT * FROM auth_user;