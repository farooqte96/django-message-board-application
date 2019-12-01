# django-message-board-application
A DJango REST API to show, create and update messages on board

This python application starts on port 8000 using "python manage.py runserver" command and has following api-endpoints:

### message/add
Add message through POST form request containing message, user, email and URL
### message/update
Update an existing message by pressing update button
### message/delete
Delete an existing message by pressing delete button
### versions/
List the versions of message supported
### versions/<int:version>/
select specific version

