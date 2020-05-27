Title: Mountain Bike Exercise App
Date: 2020-05-25
Category: Project
Tags: object-oriented programming, c#, xaml, xamarin, api, azure devops, django, python
Slug: mountain-bike-exercise-app
Author: Thomas Brunbjerg
Summary: Mountain Bike Exercise app for Android made using Xamarin Forms and Django REST Framework
featured_image: img/mtbxamarin_01.png

[![tiny]({filename}/img/mtbxamarin_02.jpg)]({filename}/img/mtbxamarin_02.jpg)
This android app served as the first semester project in my Mobile Development class at University College Lillebaelt in 2020. It tracks various exercises made specifically for people wanting to better their mountain biking training. Users can open a session to be shown a list of exercises. Selecting a single exercise will display a detail page showing the required sets and repetitions needed to complete the exercise. To track their progress, a progress bar will update, while a line chart displays the recent activity in number of completed exercises. 

Our group consisted of three people and we used **Azure DevOps** to serve as the main version control system and CI/CD pipeline. Since most of the back- and front-end code is written using Xamarin Forms, a future port to iOS is a simple process that can take advantage of the cross-platform capabilities of Xamarin. 

The underlying API was made in python using the Djange REST framework and runs on a remote linux server. The app communicates with the API to display exercise information and to update the existing exercises with the user data. 

## Technologies, Languages & Frameworks

During the project I made use of the following technologies, languages and frameworks:

- **xaml** -- used for displaying the front-end elements
- **c#** -- powers the back-end of the app and api communication
- **xamarin** - mobile development framework by Microsoft
- **python** - underlying rest api code and specification
- **django** - used to build the web API
- **azuredevops** - used for version control and as remote repository





