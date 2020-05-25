Title: MSc Dissertation
Date: 2018-08-08
Category: Programming
Tags: python, data-sharing, object-oriented programming, data formats, webprogramming, sql, user-centred design, data visualisation
Slug: msc-thesis
Author: Livia Jakob
Summary: Building a visual data sharing platform for a research group
featured_image: img/msc.png
repository: https://github.com/liviajakob/data-sharing-platform

## **Project Overview |** Visual Data Sharing Platform

**Project Submission:** August 2018

&nbsp;

[![tiny]({filename}/img/msc0.png)]({filename}/img/msc0.png)

We know that data sharing facilitates the scientific process enormously and yet not so many researchers are doing it (Schofield et al. 2009). In a survey conducted by Tenopir et al. (2011) researchers report reasons why their scientific data is not electronically available to others, with *'no place to put data'* amongst the leading reasons. My personal aim is to look for incentives that could motivate more researchers to share their data. Also, I'm very excited that I can improve my programming skills in the next couple of months and implement the first bigger project just by myself.

&nbsp;

In my MSc dissertation project I will investigate the requirements of research groups for data sharing tools and exploring techniques to visualise and contextualise data sets within such a tool. As a proof of concept a web platform for a glaciology and cryosphere research group will be implemented, with the following main functionalities:

1. enabling a research group to share data with research partners and a wider community in a utilisable way
2. enabling a research group to visualise and contextualise intermediate results for internal use

To detect researchers needs and requirements a user-centred design (UCD) approach will be applied. The UCD process will be fully documented to share challenges and lessons-learned with future data sharing platform developers.

&nbsp;

**Track my programming progress** in this GitHub repository: [https://github.com/liviajakob/data-sharing-platform](https://github.com/liviajakob/data-sharing-platform)

&nbsp;

**See my project presentation [here](https://prezi.com/view/IMPHjiggeRBnQjlWeSik/)** (Prezi presentation).

&nbsp;

## User-Centred Design Approach

Below a diagram of my *User-centred Design* workflow.

[![medium]({filename}/img/ucd.png)]({filename}/img/ucd.png)


## Architecture Design

Below a conceptual diagram of the proposed architecture design.

[![medium]({filename}/img/msc1.png)]({filename}/img/msc1.png)


## Technologies

I'm currently using (/plan to use) the following tools and technologies:

- **python3** -- back-end
- **Flask** -- python web framework
- **Flask-RESTful** -- for REST API with Flask
- **Jinja2** -- templating
- **HTML5 | CSS | JavaScript** -- front-end
- **Leaflet** -- JavaScript library for mapping
- **JSON** -- data exchange
- **gdal** -- for raster manipulation (gdal2tiles for generating tiles)
- **SQLAlchemy** -- SQL toolkit to make database flexible (also use of ORM)
- **SQLite** -- database for meta data


&nbsp;

## Sources

**TENOPIR, C., ALLARD, S., DOUGLASS, K., AYDINOGLU, A.U., WU, L., READ, E., MANOFF, M. & FRAME, M. 2011.** Data Sharing by Scientists: Practices and Perceptions. PLOS ONE, 6, e21101, 10.1371/journal.pone.0021101.

**SCHOFIELD, P.N., BUBELA, T., WEAVER, T., PORTILLA, L., BROWN, S.D., HANCOCK, J.M., EINHORN, D., et al. 2009.** Post-publication sharing of data and tools. Nature, 461, 171-173, 10.1038/461171a.