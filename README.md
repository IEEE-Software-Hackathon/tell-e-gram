<p align="center">
  <img src="https://user-images.githubusercontent.com/37483320/43250835-e547f810-90db-11e8-9b92-d5c8a3949eba.png">
</p>

# Tell-e-Gram
Tell-e-Gram is a project which will help faculty to inform students about any important information like Schedule Changes, any upcoming seminar or any other information. This information will be shared through SMS. Through other platforms like Whatsapp, sometimes information gets missed due to network glitches or any other reason. Therefore, we adopted SMS for message sharing.
Also, Additional functionality of asking queries has also been added.

# Technologies Used

This is built on django framework along with HTML, Material-CSS and Bootstrap as front-end framework. AJAX is also used to provide the touch of asynchronous manner.
To handle the message queuing, Django-background-tasks has been used which schedule the messages according to time and date set by Faculty.
Nexmo has been used as SMS API service.

# Setup Your Environment

Setup virtualenv by running command:
```
virtualenv -p python3 VirtualEnv
```
Next activate it through following command:
```
cd VirtualEnv
cd Scripts/activate
```
Install all the dependencies:
```
pip install -r requirements.txt
```
Now we are ready to boot the server
Run following command to run the localhost WSGI server of Django:
```
python manage.py runserver
```
You also have to run following command to also boot the background server:
```
python manage.py process_tasks
```
And we are done!

**For Security purposes, the credentials of nexmo has not been provided along this. Create an account on nexmo website and procure your credentials and integrate them accordingly**

# Preview of the project

> Home Page

![Home Page](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(25).png)
![Home Page](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(26).png)

> Login Page

![Login Page](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(27).png)
![Login Page](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(28).png)

> Faculty/Staff Profile Page

![Faculty/Staff Profile Page](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(29).png)

> Message Creation Page for Staff Access Only

![Message Creation Page for Staff Access Only](https://raw.githubusercontent.com/IEEE-Software-Hackathon/tell-e-gram/master/static/Images/screenshot/Screenshot%20(30).png)




