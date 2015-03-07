#Booking System

Booking System is a web application under development using Django framework.

Table of Contents
-
* [Introdution](#intro)
* [Pre-Requisites](#req)
* [Installation](#install)
* [Team Members](#team)


<a name="intro"></a>Introduction
-
Booking System is a Django based web application. The primary aim of this application is to minimize the wastage of time and money.

<a name="req"></a>Pre-Requisites
-
0. [Apache2](#apache)
0. [mysql-server](#sql)
0. [python2.7](#py)
0. [python-pip](#pip)
0. [python-mysqldb](#db)
0. [virtualenv](#venv)
0. [django 1.7](#django)
0. [mysql-python](#mysql-py)

For the installation of Requiremets listed above, run the following commands in terminal:

0. <a name="apache"></a>Apache2
 
        $ sudo apt-get install apache2

0. <a name="sql"></a>mysql-server
    
        $ sudo apt-get install mysql-server
    
0. <a name="py"></a>python2.7
    
        $ sudo apt-get install python
    
0. <a name="pip"></a>python-pip

        $ sudo apt-get install python-pip

0. <a name="db"></a>python-mysqldb
    
        $ sudo apt-get install python-mysqldb

0. <a name="venv"></a>virtualenv

        $ pip install virtualenv

0. Configuring Virtualenv

    - virtualenv venv
    - source venv/bin/activate
 
0. <a name="django"></a>Django 1.7.3

        $ pip install django==1.7.3

0. <a name="mysql-py"></a>mysql-python

        $ pip install mysql-python

0. Now run the command 

        $ pip freeze

 And the output should be similar to:
 
        Django==1.7.3
        MySQL-python==1.2.5
        argparse==1.2.1
        wsgiref==0.1.2


<a name="install"></a>Installation
-
0. Log into you mysql account using the command:
    >```mysql -u root -p```

0. Create a new database for bookingsystem inside mysql shell:
>````mysql> create database bookingsystem;````

 >```mysql> quit```

0. Clone this repository using terminal:
>``` git clone https://github.com/rvirdiz/booking_system.git ```


0. Now traverse to the directory:
> ```cd booking_system/src```

0. Edit booking_system/settings.py file. Things to be edited are:

    - In the 'DATABASES' section, replace the root in the 'USER' field with your mysql username and 1234 with your mysql password.These are the details those you entered in step 2 above.
    

0. Create a superuser for your project:
>```python manage.py createsuperuser```

    Now add Username, email(optional) and password.

0. To see the project working, shoot the following commands:
>```python manage.py migrate```

 >```python manage.py runserver 7000```
       
    Make sure you are in the booking_system/src directory in which the file 'manage.py' exists.

0. Now open your web browser with the address:

 <a href="http://localhost:7000" title="Click here to open it directly">http://localhost:7000</a>

    Enter the username and password similar to that you entered in step 6 above.

If you find any problem at any step of the installation, feel free to email us and for more detail check out the blog links given [here](#team).

#<a name="team"></a>Team Members

 

Mandeep Singh 
-
 >Contact: <mandeeps708@gmail.com>
  
 >Blog: [http://mandeep7.wordpress.com](http://mandeep7.wordpress.com) 

![Listforks](https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAACuAAAAJDE0MDZiY2QyLWQ5NjgtNDI3Ni05ZWJiLWU3NjA3MmU0ZjBlMg.jpg) 

Ramandeep Singh
-
> Contact: <ramanvirdiz@gmail.com>

 >Blog: [http://ramanvirdiz.wordpress.com](http://ramanvirdiz.wordpress.com)

<img height="200" src="https://avatars1.githubusercontent.com/u/7791892?v=3&s=400">
