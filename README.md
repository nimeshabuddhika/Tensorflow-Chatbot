# Tensorflow Chatbot

AI ChatBot that uses Python Tensorflow and Natural Language Processing (NLP) using TFLearn as a learning engine. This is capable of interacting multiple ways. Each of these module are functioning independently.

* Web interface
* Reset Api
* GUI
* CLI

And also you can train your own data model which suit to your business model. The data model format is not complex. 

### Installing

Program requires following dependencies

* Python >= 3
* Tensorflow [Click here](https://www.tensorflow.org/install/)

After successfully installation of above dependencies, you need to follow these steps in order to train the bot. 

* You can find [data model](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/Bot/content.json) from */Bot/content.json* and change the content as you wish. 
* Execute [train.py](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/Bot/train.py) file which is inside */Bot/* directory to train the model that you have prepared.
* Then, You are done!


## Getting Started

You can interact with chat bot any of these four method

#### Web interface
Django framework is used to implement this web app. You can install Django by fallowing these steps from [here](https://www.djangoproject.com/download/)

*After installation of Django framework, you need to follow these steps*

* Find [settings.py](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/Tensorflow_Chatbot/settings.py) file inside */Tensorflow_Chatbot/* directory.
* Replace 96 line according to the path of the static folder of your project under *STATICFILES_DIRS * variable. 
* Then execute following command inside the root directory.

```
python manage.py runserver
```

![web](https://user-images.githubusercontent.com/7195953/34638687-2e3b728c-f2f7-11e7-9843-0e0992c2c1d3.PNG)

#### Rest api
This app allows you to interact with bot using a rest api. You can find the [controller](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/Tensorflow_Chatbot/Api/controller.py) file from */Tensorflow_Chatbot/Api/controller.py* location. To execute this Rest api you also need to install [Django framework](https://www.djangoproject.com/download/) 


* Request URL     &nbsp;&nbsp;&nbsp;: http://127.0.0.1:8000/api
* Request Type    &nbsp;&nbsp;&nbsp;: 'POST'
* Pay load        &nbsp;&nbsp;&nbsp;: ```{"msg" : "What is your name"}```
* Response        &nbsp;&nbsp;&nbsp;: ```{"ques" : "What is your name", "res":"I'm Slack", "time" :"2018-01 10:07:32"}```


![api](https://user-images.githubusercontent.com/7195953/34638814-b46d1cbe-f2f9-11e7-916b-b79ef0eeff0c.PNG)

#### GUI

You can find UI directory from root directory and then execute [ChatView.py](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/UI/ChatView.py) file. Before executing this you need to install pygubu. Pygubu is a RAD tool which helps to develop python tknter base user interfaces.
* Download pygubu from [here](https://pypi.python.org/pypi/pygubu).
* And then extract .tar.gz file and execute following command.

```
python setup.py install
```
* Then execute [ChatView.py](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/UI/ChatView.py) file inside */UI* directory.

![ui](https://user-images.githubusercontent.com/7195953/34639820-4645c196-f30d-11e7-881a-ffb51ace6341.PNG)


#### CLI

You can interact with bot through command line interface. So find [cli.py](https://github.com/nimeshabuddhika/Tensorflow-Chatbot/blob/master/CLI/cli.py) file from */CLI* directory and then execute.

![cli](https://user-images.githubusercontent.com/7195953/34639005-60870836-f2fd-11e7-8f73-ed0d100b5521.PNG)


## Built With

* [Tensorflow](https://www.tensorflow.org/get_started/) - Build neural network
* [Django](https://www.djangoproject.com/) - Web application
* [Tkinter](https://wiki.python.org/moin/TkInter) - GUI
* [Pygubu](https://pypi.python.org/pypi/pygubu) - To Design GUI

## Author

* **Nimesha Buddhika** - [Linkedin](https://www.linkedin.com/in/nimeshabuddhika/) - *University of Moratuwa, Faculty of IT*


