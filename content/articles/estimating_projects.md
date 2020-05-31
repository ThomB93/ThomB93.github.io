Title: Estimating Software Projects
Date: 2017-10-31
Category: Article
Tags: software, architecture, estimation, projects
Slug: estimating-software
Author: Thomas Brunbjerg
Summary: This article describes various ways in which you can estimate your software projects.
report: article

[![tiny]({static}/img/article/estimating_cover.jpg)]({static}/img/article/estimating_cover.jpg)
Estimating how long a certain software project will take, or how many resources are needed to complete it is hard. Nevertheless it is necessary to do so, since people outside of the project wants to know when the the product can be delivered, at least to a certain degree of precision. There are many ways to estimate varies attributes in a project to hopefully reach some sort of conclusion that gives a more or less precise estimate. Not all projects are the same, so different techniques of estimating are needed. Software projects are inherently difficult to estimate, since so much of the estimation relies on the people themselves, and not cold numbers. How long would it take to design a relational database for this project? Hard to say. To help with this you could looks at previous projects where this task had to be done and look at how long that took, or split the task into sub-tasks and try to estimate each of them. It’s no surprise that release dates for video games are sometimes moved 8 months or even a year into the future, since there is so much risk involved in estimating these kinds of projects. As long as people are the ones who create software, there will always be some kind of uncertainty involved.

I will go through some of the estimation techniques here and describe how they work and give some examples as to how they can be used in a project. There are 2 categories of estimation techniques, core techniques and helper techniques. Estimation is done using core techniques in conjunction with helper techniques, to give a better result. I’ll describe some of the helper techniques first.

**Uncertainty Estimation** tries to give a number on how much uncertainty is involved in the final estimation. Say your project is estimated to take 10 months, with an uncertainty percentage of (+)(-)20%. This means that there is a high chance that the project could take 8 or 12 months instead. This is a good indicator on how certain you are on your estimation.

**Degradation and Counting**  tries to split each task that needs estimation into sub-tasks to then give a more precise number. You can combine uncertainty estimation with this to give each sub-task an uncertainty of their own. In this way you can minimize the overall uncertainty of the task and thereby the project by having more inputs. This is also called successive calculation.

Before any real estimation can be done we need to use the core techniques which i will describe here.

**Analogy** is the simplest form of estimation. You simple look at the numbers from a previous project that is similar to the one you are estimating on and from there, try to reach an estimation. No project is completely similar, so there will always be some risk involved, but depending on how well the previous project was documented, you could have access to a lot of information. This method could be done with knowledge of just a single project.

**Factor Assessment**  is a more complex form of estimation, that can use many different techniques of calculation to reach a precise number. You usually need information from several projects to use this method and there has to be calculable information in your project, such as budget, team size, working hours etc.

**COCOMO** is one of these techniques of factor assessment to estimate a software project. There are 2 different types of formula that are important using this method as shown below:

[![small]({static}/img/article/estimate_formula.png)]({static}/img/article/estimate_formula.png)

The first of these formula describes an estimation of the number on man months (MM). KDSI is lines of code * 1000 and the the rest of the numbers are factors that gives a number on how difficult a certain task is. If it is below 1 it means it is easier, above 1 means it is harder. These numbers are found using tables of numbers from previous projects. TDEV is total number of development months.

You shouldn’t estimate only once during the project lifetime, but always try to refine your estimations as your gather new knowledge. If a task needs to be done more than once, use your estimation on the first time the task was done to estimate the rest. Hopefully towards the end of the project you will have a precise number on how long and how much is needed to complete the project. If you don’t have much data yourself, use the many collections of data available in your field as a starting point.