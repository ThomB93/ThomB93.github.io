Title: Nolek Admin System
Date: 2020-05-25
Category: Project
Tags: wpf, windows, presentation, foundation, c#, xaml, sql, forms
Slug: nolek-admin-system
Author: Thomas Brunbjerg
Summary: Desktop Administration System created as part of my final semester project in CS class
featured_image: img/nolek_cover.gif

This application was developed in coorperation with Nolek Leak Testing in Kolding, Denmark. The purpose of the application was the administration of equipment & machines, with the end goal of replacing the current software solution. In addition, a user should be able to print a 'service report' after performing a service check, while also being able to see a log of each item. 

While we did not manage to fulfill all of these use cases, the application was succesful in giving me a broader knowledge of .NET development patterns and the SCRUM methodology which was used intensively in the project. You can read more about SCRUM at [this article]({filename}/articles/scrum.md). Windows Presentation Foundation (WPF) was used as the framework of choice and the desktop based user interface was developed using XAML. 

The project was split into 8 sprints, each one focusing on certain aspects and use cases of the system. To track the project as it went along we made use of the project management platform [Taiga](https://taiga.io/). As a version control system we used Github. 

[![tiny]({static}/img/nolek_01.png)]({static}/img/nolek_01.png)

MVVM (Model, View, ViewModel) was used as the architectural pattern and guided how the project was structured, both but in terms of folder structure and how the source code was managed. In short, it means that we seperate the UI (View) from the data layers. Each view then has its own view-model, which acts as a binding layer between the view and the model (data). When working in WPF, this is especially useful, as you can quickly get bound up in code-behind files from the view. 

[![small]({static}/img/nolek_02.png)]({static}/img/nolek_02.png)

To persist data we used a standard MSSQL database with Entity Framework acting as the ORM. While developing the application, the database was stored locally, but in a production setting it would be placed on an external server.

**Project Planning**

During the planning phase we made use of UML diagrams, such as sequence diagrams and class diagrams, to gain a better understanding of our domain and how the application should be structured. We went 'database-first', thereby designin the EER diagram as the first step. Nowaways, however, this is NOT the recommended way to approach a project of this scope. It worked in our case, since the DB specification was quite clear from the beginning and did not require any changes. 

[![medium]({static}/img/nolek_03.png)]({static}/img/nolek_03.png)

