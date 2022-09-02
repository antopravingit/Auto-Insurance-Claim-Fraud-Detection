# Insurance Claim Fraud Detection 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)
  * [Credits](#credits)


## Demo
Link: [https://auto-insurance-fraud-detection.herokuapp.com/](https://auto-insurance-fraud-detection.herokuapp.com/)

![Alt Text](https://github.com/antopravingit/Insurance-Claim-Fraud-Detection/blob/main/insurance-fraud.gif)

## Overview
The goal of this project is to build a model that can detect Auto insurance claim fraud. The challenge behind fraud detection in machine learning is that frauds are far less common as compared to legit insurance claims. This type of problems is known as imbalanced class classification.Frauds are unethical and are losses to the company. By building a model that can classify auto insurance fraud, I am able to cut losses for the insurance company. Less losses equates to more earning.

## Motivation
I learned a lot from Kaggle,Github,Youtube,Medium and many other community. Thanks to all the people who took time to post all their learnings to help others. I felt it is my time to give it back.

## Technical Aspect
This project is divided into two part:
 1. Exploratory Data Analysis
 2. Due to the imbalanced dataset, SMOTENC is used before trainig the model
 3. Training with 8 different Machine learning models, compare the results. Choose the best model
 4. Deploy the ML model to Heroku using FLASK

 

## Installation
The Code is written in Python 3.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
## Deployement on Heroku
Login or signup in order to create virtual app. You can either connect your github profile or download ctl to manually deploy this project.

[![](https://i.imgur.com/dKmlpqX.png)](https://heroku.com)

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

## Directory Tree 
```
├── template
│   ├── home.html
├── Fraud_detection_model.ipynb
├── Procfile
├── README.md
├── ada.pkl
├── app.py
├── insurance fraud claims.csv
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/rowhitswami/Indian-Currency-Prediction/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/antopravingit/Auto-Insurance-Claim-Fraud-Detection/issues). Please include sample queries and their corresponding results.

## Credits
- [Insurance fraud dataset Download](https://www.kaggle.com/datasets/buntyshah/auto-insurance-claims-data) - This project wouldn't have been possible without this data from Kaggle.
