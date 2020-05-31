Title: Loevbjerg Rema 1000 Sommerhusudlejning
Date: 2017-10-31
Category: Project
Tags: object-oriented programming, webprogramming, sql, umbraco, aspnet, c#, javascript, angular, cms
Slug: loevbjerg-rema-1000-sommerhusudlejning
Author: Thomas Brunbjerg
Summary: Holiday Cottage Rental site made using Umbraco CMS
featured_image: img/lr1000_01.png

## **Project Overview |** Holiday Cottage Rental Site

[Link to the site](http://www.lovbjerg-rema1000-sommerhus.dk/)

This project was completed during my 3-month internship as a web-developer at [CodeOptimus](https://www.codeoptimus.dk/) in 2017. The site was made using the **Umbraco CMS** as the driving core, while the design was mostly implemented with the help of bootstrap and a few smaller css frameworks. It is entirely written in C# and Javascript on top of the ASP.NET platform. During development I gained knowledge of content management systems and their implementention in projects focused on non-technical users, as well as the workflow of creating a user-friendly design that targets a wide audience. While the majority of the design is based on templates, the final design was the result of heavy manipulation of the underlying CSS code. 
[![small]({static}/img/lr1000_03.png)]({static}/img/lr1000_03.png)
Since the content of the site is managed by Umbraco, changing the various elements, such as headers, textblocks and images, are made simple for the users wanting to add new rental cottages, add new images or change descriptions etc. In addition the layout is responsive, allowing the site to be viewed on mobile devices.
[![small]({static}/img/lr1000_04.png)]({static}/img/lr1000_04.png)
Users can perform bookings via a form, which then validates the input against the database. Some client validation is also handled by a few javascript frameworks. To display the location of the cottages on the site, I integrated Google Maps with Umbraco, meaning that users only have to input the address in the CMS for the map to work. 
[![small]({static}/img/lr1000_05.png)]({static}/img/lr1000_05.png)
The project was completed in late October 2017 before being handed over to the customer for approval. The site is still in use today for handling rentals of holiday cottages by employees in Rema 1000 and Loevbjerg. 

## Technologies, Languages & Frameworks

During the project I made use of the following technologies, languages and frameworks:

- **c#** -- back-end code driving the asp.net application and the Umbraco CMS
- **javascript** -- used for powering various front-end JS frameworks such as the calendar
- **angular** -- powers the front end components of Umbraco CMS
- **sql** -- data is stored in a MSSQL database
- **bootstrap** -- is used to implement the overall design, look and feel
- **umbraco** -- runs the content management part of the website
- **razor** -- used by ASP.NET to embed back-end code
- **jquery** -- helps in selecting elements based on user input