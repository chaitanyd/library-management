# library-management
Library Management System

Project File Structure


1. Installation of Django framework
    pip install django
    
2. Create a project and an app
    django -admin startproject TechVidvanLibrary
    python manage.py startapp home
 
3. Models.py
    Models.py file does the database connectivity.
        - UserExtend() model extends the user model as the user model contains only email, first name, last name and password. As we also want to save the phone number of a person           in the database, we create this model.
        - The AddBook() model stores the data of books that are added in the library.
        - IssueBook() model stores the information of the book that is issued and also the studentid of the student to whom the book is issued.
    

 4.Admin.py
    The models that are created in the models.py file are registered in admin.py. By adding models in admin.py these tables can be seen in the database.
       -  register(): It helps to register the model in the database...To see the tables we need to run migrations
            python manage.py makemigartions
            python manage.py migrate
            
       - To access database we have to create one superuser..
            python manage.py createsuperuser

 5.Urls.py
    If a user tries to access urls other than these he/she will not be able to access those urls. Create a urls.py file in the home folder.
        -  path(): It returns the element that is included in the url patterns.
        
 6.Views.py
    AddBook() - addbook() redirects to the page where the book can be added.
                AddBookSubmission() handles the backend of the adding book page. It stores bookid, book name, subject and category entered by the user in the database.
                
    Issuebook() - bookissue() redirects the user to the page where the book can be issued by entering the details of bookid and studentid.
                  issuebooksubmission() handles the backend of the form. It takes the information of bookid and studentid and stores it in the database and also it changes the                         status of the book from Not-Issued to Issued in the database as well as in the table that is displayed on the dashboard.
