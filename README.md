
# Geo Location web service

A Django web service to store user name, latitude, longitude, address 
which is obtained using google maps reverse geocoding API
## Frontend

Open geolocation.html file in any browser.
Enter your name. On clicking get location button browser asks your permission to access
location.

Once google maps API is successful you will get a submit button.
Click it to save your address on Django webservice.

#### Put your Google Maps API key in variable mapsAPIKey is geolocation.html file
#### Right now validation for empty input field is not provided. 
## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Install dependencies

```bash
  pip3 install Django~=3.1
  pip3 install djangorestframework
  pip3 install django-cors-headers
```

Go to the project directory

```bash
  cd my-project
```

Run database migrations
```bash
  python3 manage.py makemigrations
  python3 manage.py migrate
```

Create SuperUser

Call the following command, in the same directory as manage.py, 
to create the superuser. You will be prompted to enter a username,
 email address, and strong password.

 ```bash
 python3 manage.py createsuperuser
 ```

Start the server

 Go to root folder of Project  .It has manage.py file.
 

```bash
  python3 manage.py runserver
```

Browse to http://127.0.0.1:8000/admin and login using
credential used to register SuperUser.

## User list

Browse to 

http://127.0.0.1:8000/admin/catalog/person

Click on user to select and delete if not found suitable.

You can also browse to see the availabe list of users and add to it.

http://127.0.0.1:8000/catalog/people