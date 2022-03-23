# Rate my school web application ([Django](https://www.djangoproject.com/))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Directory inforamtion:
```web_application/RateMySchoolProject/```

Rate my school provides ratings of universities and professors in developing countries. Users can search for colleges and professors and see their ratings. The overall ratings will be graphically and interactively displayed. Written evaluations will also be displayed in a nice card view. Users can post written feedback and these feedbacks can be upvoted and downvoted by other users. In order to rate or vote for/against rates, users have to register and log in. Moreover, users will be given badges like gold, silver, and platinum depending on their participation and their credibility.This will be measured based on how many times they rated and how many upvotes/downvotes they get. And there will be a verification feature where notable will be verified in which case they will have a special check mark on their name. The web app will also use a profanity check library or a machine learning model to check for abusive words before a user posts anything. Other users can also report in which case they can be blocked based on the approval of the adminstrator.
<hr />
Suplements:

![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white) 

# Explore
## Set up
Clone the repository

```
$ git clone https://github.com/Tesfa-eth/web_application.git
```
```
$ cd web_application
```

Create a virtual environment to install dependencies in and activate it:
```
$ virtualenv env
$ source env/bin/activate
```

Then install the dependencies:

```
(env)$ pip install -r requirements.txt
```

Note the ```(env)``` in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by ```virtualenv2```.

Once ```pip``` has finished downloading the dependencies:
```
(env)$ cd RateMySchoolProject
```

```
(env)$ python manage.py runserver
```
And navigate to:
```
http://127.0.0.1:8000
```

# Walkthrough
Once you do all this and navigate to ```http://127.0.0.1:8000```. Go to ```College Ratings```. There, you will be able to search universities. The search bar will bring you recommendations as you start to type in. If you don't know what to search for just type ```uni```. Then you can search for universities and see their over all ratings in an interactive graph as well as see the average ratings and individual ratings and written feedbacks.
<img width="960" alt="chrome_CPlG4CFwlK" src="https://user-images.githubusercontent.com/62855279/159392394-7bee3f8a-e18c-40c0-a459-0f454761980f.png">

