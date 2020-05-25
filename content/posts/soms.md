Title: Self-Organising Maps
Date: 2018-03-13
Category: Spatial Analysis
Tags: machine learning, R, spatial analysis, statistics, data exploration, data visualisation
Slug: soms
Author: Livia Jakob
Summary: Using machine learning to explore spatial data (Scottish deprivation data)
featured_image: img/soms.png
repository: https://github.com/liviajakob/self-organising-maps/
report: img/docs/SOM_report.pdf


## **Project Overview |** Self-Organising Maps

[![tiny]({filename}/img/soms.png)]({filename}/img/soms.png)
This project applies the Self-Organising Maps (SOM) machine learning technique to Scottish deprivation data from Edinburgh. SOMs offer insights that can't be explored or displayed with the linear deprivation indices. I used the **kohonen package** within the software **RStudio**. Code can be found in my [GitHub repository](https://github.com/liviajakob/self-organising-maps/).

I think the data exploration etchnique SOMs is a very powerful technique to analyse spatial data, especially when the data is multi-dimensional.

Read more about Self-organising maps for spatial data in my [blog post](http://www.geo-blog.com/soms-for-geographical-data/).

## What are SOMs?
Self-Organising Maps (SOMs) are a type of unsupervised Artificial Neural Networks (ANNs). They were developed by Teuvo Kohonen (1982) and are mostly used for clustering, visualisation and data exploration. SOMs reduce n-dimensional data and display it on the two-dimensional map where similar data is placed into the same grid cells.

## Training and Clustering

The study uses the 2016 SIMD dataset containing 26 deprivation variables (excluding absolute measures), an overall rank and rankings over each of the 7 domains (ncome, employment, education, health, access to services, crime and housing). To closely monitor deprivation patterns, the study area was reduced to the 597 data zones in Edinburgh. The 26 variables were summed up within each of the themes and the SOM was then trained with seven variables representing the seven themes. After the SOM training seven clusters were created using the hierachical clustering method.


## Results

This section will show brief results of the study. For more information read the [report](img/docs/SOM_report.pdf).

[![large]({filename}/img/soms3.png)]({filename}/img/soms3.png)

The component planes show the distribution of each variable in the SOM. Red values indicate high disadvantage, whilst blue values represent low disadvantaged. The planes further show visually that income, health, employment and education are correlated. The numbers represent the seven clusters.

&nbsp;

By means of component planes analysis and display of the results on a geographic map, the clusters were characterised to facilitate the interpretation. Note that the cluster descriptions are not purely based on sci- entific knowledge, moreover they aim to tell a narrative backed by common knowledge about the city.

[![large]({filename}/img/soms2.png)]({filename}/img/soms2.png)

Characteristics of the seven clusters. The node background colours represent the seven clusters. The codes show the seven variable properties for each neuron, with larger symbols indicating higher disadvantage. They are dis- played to visualise similarity and differences between adjacent neurons.


&nbsp;

### Cluster Charactersitics

- **Cluster 1 (7%) | The Precariats --**
The Precariats is a cluster defined by very high disadvantage within the income and employment domain, low education and health issues, whilst access, crime and housing do not seem to be a major issue. The Pre- cariats are the poorest and most deprived cluster.

- **Cluster 2 (23%) | Rough Edinburgh --**
The inhabitants of *Rough Edinburgh* share similarities with *The Precariats* but are less vulnerable. How- ever, they still score very low within the domains income, employment, education and health. Typical “Rough Edinburgh” districts are areas with social housing such as Dumbiedykes.

- **Cluster 3 (13%) | The Wealthy Commuters --**
The Wealthy Commuters are the cluster most disadvantaged by access – but by choice. Apart from the ac- cess domain they show very low disadvantage amongst all the themes. They typically live on the outskirts or in suburban areas where they are house owners and commute to work every day.

- **Cluster 4 (41%) | The Waitrose Shoppers (Edinburgh Posh) --**
This cluster is defined by a uniformly low disadvantage across the seven themes. Typical middle class families and professionals with high income and education living in urban and suburban areas belong to this cluster. Areas such as Marchmont and Stockbridge are typical for this cluster.

- **Cluster 5 (3%) | The Urban Intermediates --**
This cluster is defined by excellent access and intermediate characteristics amongst the domains income, employment, health and education. It is noticeable that there is a relatively high crime rate and rather low housing conditions.

- **Cluster 6 (1%) | The Crime Triangle (Edinburgh Nightlife) --**
The Crime Triangle is defined by very high crime and bad housing. It represents only a very small area in the city centre nearby Princess Street. Data zones within this cluster are not a typical living area but rather an area where people congregate and where young people enjoy the nightlife, which explains the high propor- tions of crime rates per inhabitants.

- **Cluster 7 (12%) | The Hotchpotch --**
The Hotchpotch is characterised by very bad housing and excellent access. It encompasses areas in the city centre with a high proportion of students and presumably flat shares, but also more ethnic areas near to the city centre.

&nbsp;

[![medium]({filename}/img/soms4.png)]({filename}/img/soms4.png)

&nbsp;


## Sources

**Kohonen, T. 1982.** Self-organized formation of topologically correct feature maps. Biological Cyber- netics, 43, 59-69, 10.1007/BF00337288.

**Kohonen, T. 2001.** Self-Organizing Maps. 3rd ed. Berlin Heidelberg: Springer-Verlag Available at: www.springer.com/gb/book/9783540679219 (Accessed March 29, 2018).

**Skupin, A. & Agarwal, P. 2008.** Introduction: What is a Self-Organizing Map? In Agarwal, P. & Skupin, A., eds. Self-Organising Maps. Chichester, UK: John Wiley & Sons, Ltd, 1–20., 10.1002/9780470021699.ch1.