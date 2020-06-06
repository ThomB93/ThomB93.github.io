Title: Extreme Programming
Date: 2017-01-01
Category: Article
Tags: extreme, programming, xp, methodology, agile
Slug: extreme-programming
Author: Thomas Brunbjerg
Summary: Describes the methodology of Extreme Programming and its benefits
report: article

XP is yet another agile software development methodology, that focuses on being able to frequently act on changing customer requirements while also having frequent iterations and releases. There are many aspects to XP and I'll go through the most important processes involved and explain how they fit together to hopefully being able to deliver a software product by the end of the project cycle.

[![small]({static}/img/article/xp_01.png)]({static}/img/article/xp_01.png)

Before any iteration can begin, you need to establish the user stories, which are the customer requirements written in an informal manner by the customer, so as to sort of 'tell a story' as to what the requirement needs to do. An example would be: "As a customer, I want to be able to check my added items so that I can purchase them later." You can use this format for all the user stories, showing WHO needs to do the action, WHAT they need to do, and WHY.

Release Planning is a meeting where the release plan is created, which contains all the user stories and the iterations in which they are planned. Go through each user story and estimate it in a number of weeks, 1-2 or 3. Then have the customer pick the ones with the highest priority. Don't plan out the iterations in detail, that comes later. There are basically 4 variables for planning a release: time, scope, resources, and quality. All these variables affect one another and it is up to the team to focus on which are the most important.

Iteration Planning is a meeting held just before an iteration starts (Also called a project heartbeat). The customer chooses which user stories go into the iteration and acceptance tests are created for each user story, which are scenarios specified by the customer in which the user story is considered done. If an iteration has already been completed, use the projected velocity from the last iteration to estimate how many user stories can be completed. I'll explain project-velocity in a short bit. Each user story for the iteration is broken down into tasks for and by each developer. A task should last 1-2 or 3 days. Estimate the total days of all the tasks and make sure they don't go above the project-velocity. Don't change the estimates to fit a needed total estimate, remove some user stories if you must.

[![small]({static}/img/article/xp_02.png)]({static}/img/article/xp_02.png)

Project Velocity is a number describing how much work is getting done in each iteration. Calculate it by adding up all the user stories that were finished in the first iteration, as well as the tasks. In the next iteration, the customer is allowed to select user stories with estimates that total up to the project-velocity. Calculate the project-velocity after each iteration, and if it falls dramatically, consider holding a new release planning meeting. The farther you are into the project, the better your estimations.

During the release planning, you can choose to plan either in regard to time or scope. When planning in regard to time, use this calculation:

    (Number of iterations) * (Project Velocity) = User Stories to be completed

When instead planning by scope use this calculation:

    (Total weeks of user stories) / (Project Velocity) = Iterations needed before release

Both of these numbers can give an indication of how long a project will last and how much work can be completed.

If after an iteration some the user stories fail their acceptance tests, they must be included in the next iteration and new acceptance tests must be completed.

An iteration should last about 1-3 weeks, but make sure each iteration has more or less the same length, as it makes estimation easier. If you notice you can't finish all the user stories for the iteration, consider holding another iteration planning meeting during the iteration, and reschedule your tasks. Never add more functionality than what is needed.

Another important aspect is XP is automated testing and especially unit testing. All code should have unit tests attached. Write the test first, then code. No code may be released that has not passed all its unit tests. This also ensures that you don't add unnecessary code, as it only has to pass all unit tests and nothing more.

Spike Solutions are small programs meant to explore a certain technical problem and hopefully figure out a solution. Put a few developers on the problem and let them crunch out a solution, without concerning themselves with anything else during that time.