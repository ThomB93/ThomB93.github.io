Title: Covariance & Correlation
Date: 2020-05-29
Category: Article
Tags: covariance, correlation, machine learning, ml
Slug: covariance-correlation
Author: Thomas Brunbjerg
Summary: Outlines the basic principles of covariance and correlation and how the two are related
report: article

**Variance:**

1. Find the mean of the data points
2. Calculate the distance to each data point from the mean.
3. Subtract the mean from the distance value and square it. Do the same for all data points and sum them. Then divide that sum by the number of observations -1.
4. This gives you the variance.

[![tiny]({static}/img/article/covCor_01.png)]({static}/img/article/covCor_01.png)

**Question:** Do the measurements taken in pairs tell us something that the individual measurements do not? Covariance tries to answer this question.

**Covariance:**

* Can classify 3 types of relationships:
    * Positive trends
    * Negative trends
    * No trend
* By itself, it is not very interesting
* Leads to correlation

$$\frac{\sum(x-\bar{x})(y-\bar{y})}{n-1}$$

**How to calculate?**

1. For each data point (x and y, subtract the mean and sum them. Then divide that sum by the number of observations -1. 
    * When both x and y are less than their respective means, multiplying them together gives a positive value.
    * When both x and y are greater than their respective means, multiplying them together gives a positive value. 
2. If the covariance value is positive, we have a positive trend. If the covariance value is negative, we have a negative trend. If the covariance value is 0, we have no trend. 
3. The covariance value does not tell us anything about the slope of the line. It is hard to interpret.

[![tiny]({static}/img/article/covCor_02.png)]({static}/img/article/covCor_02.png)

**Why is the covariance value hard to interpret?**

1. The covariance for X with itself, is the same thing as the estimated variance for X.
2. The covariance value can change when the relationship does not change.
    * E.g. Multiplying each value of X by 2, will produce the same slope, but a new covariance value.
3. Covariance values are sensitive to the scale of the data
4. Are used in principal component analysis

**Correlation** describes relationships and is NOT sensitive to the scale of the data.

* The closer the data is to the line, the more X can tell us about Y.
    * If data points fall close to the line, the relationship between X and Y is strong
    * If data points fall far away from to the line, the relationship between X and Y is weak  
     
We use correlation to **quantify the strength of a relationship**.

[![tiny]({static}/img/article/covCor_03.png)]({static}/img/article/covCor_03.png)

* Correlation = 1, when the line goes through every data point in a positive trend.
* Correlation = -1, when the lines goes through every data point in a negative trend
* Correlation = 0, when a value on the X-axis does not tell us anything about the value on the y-axis
* With small datasets, we should have low confidence in the correlation value.
    * With 2 data points, there is no confidence in the correlation value, as we can always draw a straight line through them.
    * The probability that we can draw a straight line through every point gets smaller the more points we have.
    * When talking about correlation, we are only talking about straight lines.
    * P-value tells us the probability that randomly drawn dots will result in a similarly strong relationship or stronger.
        * Smaller p-value = more confidence in predictions
        * P-value gets larger the less data we have
    * Adding data does not always improve the correlation value.
    * You can calculate correlation if you know the variance and covariance 
$$Correlation = \frac {Covariance(X, Y)}{\sqrt{Variance(X)}\sqrt{Variance(Y)}}$$
    * Denominator makes the covariance to be a number between -1  to 1. Ensures that the scale does not affect the correlation value.
        * E.g. if correlation is 0.9 and p-value is 0.03, then there is a 3% chance that random data could produce the same relationship or a stronger one.
