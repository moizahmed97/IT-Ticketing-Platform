# IT Ticketing Platform

Managing and assigning IT issues at any organization is a major problem. A lot of issues slow down work at the company and with remote work it has become harder to issue and track problems. 

This project built using Django backed with an SQL database and  is meant to solve the above problem. 

It consists of 3 types of users 

1. Admin 
2. Technician 
3. Issuer (End User)

## End User or Issuer 
The End User can 
- Create new issues
- Add screenshots and some explanation. 
- Assign a priority to the issue and track its progress (Ongoing, completed, unassigned)
- Setup the profile with AnyDesk or TeamViewer ID.

## Admin 
The created issue is then forwarded to the admin who can 
- Assign issues to the technician and track its progress 
- View all the ongoing and completed issues
- Generate reports by Issue Type and Technician

## Technician
- View all pendng issues 
- View history of all completed issues assigned to them 
- Change the status of the assigned issue 
- Add comments and details to an assigned issue

The Admin has elevated priveleges and can create, update or delete any user in the system. 

### Miscellanous functionality 
- Users can Reset the password using their email IDs.
- Recieve email notifications when involved in an issue when its status has changed 

# Downloading and using the code 

Clone the Github Repository 

Update database migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```

To create a superuser (Admin)

```
python manage.py createsuperuser
```

To start the server 

```
python manage.py runserver
```

The app should start on `localhost:8000`

The admin view can be accesed at `localhost:8000/admin`


