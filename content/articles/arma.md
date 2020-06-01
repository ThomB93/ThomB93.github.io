Title: Autoregressive Moving Average Model
Date: 2020-05-29
Category: Article
Tags: arma, autoregressive, moving average, machine learning, ml, time series
Slug: armamodel
Author: Thomas Brunbjerg
Summary: Describes the ARMA model in relation to Machine Learning and Time Series Data
report: article

The ARMA Model is a merger between the AR (Autoregressive) and MA (Moving Average) models. By combining the two, we produce a more sophisticated model for making predictions on time series data. The AR part makes the variables be regressed onto their own past values, while the MA part takes unexpected effects into account. Note that the time series used must still be stationary for the AR part to be effective. 

So what does the model consist of? Let's take a look at each of the parts to gain a better understanding of the model as a whole.

**AR**: Uses a linear combination of past values of the variable we want to predict. The 'Auto' part indicates that it is a regression of the variable onto itself. 

**MA**: Uses past forecast errors in a linear regression of the variable to make predictions. 

Now that we have a rough understanding of each part, let's dive deeper into an example of the ARMA model in action. Let's say we want to predict how many lightbulbs will be sold given some past sales numbers from previous months. First, let's take a look at the equation below, which corresponds to an **ARMA(1,1)** model.

The orders (1,1) of the model, determines the number of time lags that we include for each part. Thus if we change the model to have the orders of (2,1), then we include time lags from both last month and 2 months ago in the equation. These are normally given as (p,q), with 'p' determining the order of the AR part and 'q' determining the order of the MA part. By excluding one of these orders, you can create either an AR or an MA model. 

## $$l_t=\beta_0+\beta_1l_{t-1} + \phi_1\epsilon_{t-1}+\epsilon_t$$

To gain a better understanding, let's define each term as it is written:

**l<sub>t</sub>** is the number of lightbulbs that we should sell this month. In other words, this is the number that we want to predict using our ARMA model.

**$B$<sub>0</sub>** is a coefficient or constant that we include - also called a 'Shock term'. 

**$B$<sub>1</sub>** is the autoregressive coefficient at lag 1.

**l<sub>t-1</sub>** is the number of light bulbs that was sold last month (1 from the current month).

**$\phi$<sub>1</sub>** is another coefficient or constant that we include.

**$\epsilon$<sub>t-1</sub>** is the error, or 'Shock Term' from the last month (1 from the current month).

**$\epsilon$<sub>t</sub>** is the error from the current month.

There are some unknowns in this equation, such as the light bulbs that we need to sell this month and the error for the current month. However we *do* have acccess to all past knowledge. As such we can form a new equation for our predictions without these unknown values. 

## $$\hat{l_t}=\beta_0+\beta_1l_{t-1} + \phi_1\epsilon_{t-1}$$

Now we have an equation to help us predict the number of light bulbs we should sell this month. 

## How to use the model in Python?

## How do you determine the AR and MA orders?
To determine the order values, we make use of Autocorrelation (ACF) for the MA part and Partial Autocorrelation (PACF) for the AR part. Our goal is to use lags that are correlated the most to the value we want to predict. So how do you use these methods for determining the orders?

[![small]({static}/img/article/arma_acf_pacf.png)]({static}/img/article/arma_acf_pacf.png)

**ACF**: Measures the moving average for the time series and therefore helps determine the MA order. As an example, 

