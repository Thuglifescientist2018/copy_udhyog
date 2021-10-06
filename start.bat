@echo off
start "" http://127.0.0.1:8000
cmd /k "cd /d C:\Users\Shashwat Dahal\.virtualenvs\new_software_order-YNj-0wlu\Scripts & activate & cd /d  D:\new software order\copy_udhyog & python manage.py runserver"
