Title: Linear Regression
Date: 2020-06-07
Category: Article
Tags: linear, regression, machine learning, ml
Slug: linear-reg
Author: Thomas Brunbjerg
Summary: Describes Linear Regression and how it can help you make accurate predictions in ML models
report: article

**The general idea:**

1.	Use least squares to fit a line to the data
2.	Calculate **R<super>2</super>** (should be large)
3.	Calculate a p-value for **R<super>2</super>** (should be small)
    * We calculate p-value because **R<super>2</super>** is not reliable in itself.

[![tiny]({static}/img/article/linear_reg_01.png)]({static}/img/article/linear_reg_01.png)

**Example:**

1. Fit a horizontal line onto the data and measure the distance from the line to the data points, square them and then add them up.
    * The distance from the line each data point is called a residual.
    * We square the distance to avoid negative numbers.
2.	Rotate the line and measure the distances again, generating a new sum.
3.	Repeat the process several times
4.	Plot the sum of squared residuals against the rotations and find the rotation with the lowest sum. This one will fit the data best.
5.	We now have an equation for the line after it has been fitted.

[![tiny]({static}/img/article/linear_reg_02.png)]({static}/img/article/linear_reg_02.png)

**R<super>2</super>**:

1.	Shift all the data points to the y-axis (we are only interested in one feature)
2.	Find the average data point.
3.	Sum the squared residual for each data point (the distance from the average)
$$SS(mean) = (data - mean)^2$$
$$Var(mean) = \frac{(data - mean)^2}{n}$$
        * 'n' is the sample size
        * This is the average sum of squares per mouse
$$SS(fit) = (data - line)^2$$
$$Var(fit) = (data - line)^2 / n$$
4. **R<super>2</super>** tells how much variation in feature X can be explained by taking feature Y into account. 
$$R^2 = \frac{Var(mean) - Var(fit)}{Var(mean)}$$
    * E.g. if **R<super>2</super>** is 0.6, then there is a 60% reduction in variance when we take feature Y into account.


[![tiny]({static}/img/article/linear_reg_03.png)]({static}/img/article/linear_reg_03.png)

**Least Squares** will cause any term that makes SS(fit) worse to be multiplied by 0 and thus no longer exist an have an effect on the prediction.
* But, the more features we add, the more chance for random events to reduce SS(fit)
* The solution is to have an adjusted **R<super>2</super>**, that considers the number of parameters. 
If we only have 2 data points, then **R<super>2</super>** will always be 1 = 100%.
 
 $$F=\frac{SS(mean) - SS(fit) / (p_{fit} - p_{mean})}{SS(fit) / (n - p_{fit})}$$
 
How do you determine if **R<super>2</super>** is statistically significant?

* Calculate a p-value for **R<super>2</super>**
* The p value comes from 'F'
    * The p numbers determine the 'degrees of freedom'
    * Turns sums of squares into variances
* P(fit) = number of parameters in the fit line (for a 2-dim line we have 2, the slope is the 'extra' parameter)
* P(mean) = number of parameters in the mean line (for a 2-dim line we have 1)
* The more parameters you have in your equation, the more data you need to make estimations. 
* Numerator of F: Variance explained by the extra parameter(s)

How to turn F into a p-value?

1. Calculate F for a ton of generated random datasets
2. Insert each value in a histogram
3. The p-value is the number of more extreme values divided by all the values.
4. You can also use the line of the histogram to calculate the p-value
5. The p-value will be smaller when there are more samples relative to the number of parameters in SS(fit)
