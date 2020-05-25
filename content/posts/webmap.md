Title: SVG Webmap with Database
Date: 2017-12-12
Category: Websites
Tags: webprogramming, sql, maps, webdesign, spatial databases, python, svg
Slug: webmap
Author: Livia Jakob
Summary: Implementation of a generic SVG webmap using data stored in a database
featured_image: img/webmap.png
projectlink: https://www.geos.ed.ac.uk/~s1790173/cgi-bin/fields/fields.py


## **Project Overview |** Fields and Finds

![tiny]({filename}/img/webmap.png)


For this project I have developed a database model and implemented it in an Oracle database. 

The map data is retrieved by a python script which accesses the Oracle database and queries it with SQL queries. The python script displays the data on a web server (the webmap is created on-the-fly). The SVG map is created as such that changing the data inside the database would change the content of the map.

The webmap is **interactive** (hovering, clicking, querying and display/hide layers) which is programmed in JavaScript.

&nbsp;

**Explore the result:** [https://www.geos.ed.ac.uk/~s1790173/cgi-bin/fields/fields.py](https://www.geos.ed.ac.uk/~s1790173/cgi-bin/fields/fields.py)

&nbsp;

## **Database Model |** Implemented in Oracle

[![medium]({filename}/img/webmapdb.png)]({filename}/img/webmapdb.png)

&nbsp;
&nbsp;


## **Example Screenshots |** [www.kindrogan.geo-blog.com](www.kindrogan.geo-blog.com)

&nbsp;

[![medium]({filename}/img/webmap1.png)]({filename}/img/webmap1.png)

[![small]({filename}/img/webmap2.png)]({filename}/img/webmap2.png)

[![small]({filename}/img/webmap3.png)]({filename}/img/webmap3.png)

