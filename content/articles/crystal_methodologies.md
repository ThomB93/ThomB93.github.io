Title: Crystal Methodologies
Date: 2017-10-31
Category: Article
Tags: software, architecture, crystal, methodologies, cockburn
Slug: crystal-methodologies
Author: Thomas Brunbjerg
Summary: 
report: article

[![tiny]({filename}/img/article/crystal.jpg)]({filename}/img/article//crystal.jpg)
[Crystal](https://en.wikiversity.org/wiki/Crystal_Methods) is a set of methodologies created by Alistair Cockburn, to differentiate projects of different sizes, scope and criticality. It’s easy to understand that the software needed for a nuclear reactor is much more life-critical than say a video-game. In more serious projects,the amount of testing, formal procedures and documentation becomes increasingly higher. In an ideal world, no mistakes are made, but of course this is not feasible in any project. 
[![small]({filename}/img/article/crystal_table.png)]({filename}/img/article//crystal_table.png)
Each color represents a certain project size in terms of the number of people working on it. So, if you are making a game and your team consists of 45 people, you would have a **C80** project. While there are certainly differences between the crystal types, some common methods persist - like having constant feedback from the customer, having many iterations, and giving each member at least 2 hours of uninterrupted work each day. You should always opt to pick the simplest of the crystals, but don't go too simple. This is a perfect occasion to make use of this famous quote:

>*Everything should be made as simple as possible, but not simpler.* - Albert Einstein

Clear, Yellow and Orange the most commonly used, so most project will fit into these categories. Likewise, not many projects are life critical, so most will end up in the upper part of the matrix.

**Crystal Clear** is the simplest of the crystal types. Only 3 roles are needed: a Sponsor, who is the person or company the software is released to and who pays for it; a senior designer who can design the initial release and generally help the less experienced members of the team, and of course the programmers who do the hard labor. There can be more than one person in each role. The project is mostly seen as informal and progress is only measured in released software cycles.

**Crystal Yellow** has more members and so needs more management (obviously). Perhaps it is now a good idea to split the developers into their own rooms, while still communicating and giving each other feedback. It’s important that everyone shares the same vision of the project and that further planning is being made for each iteration, though don't overdo it. The atmosphere is still informal and extensive documentation should be avoided as to no derail the project. 

**Crystal Orange** can have up to 40 team members, which means more roles for the team. A project manager handles how the project is progressing and makes changes to the iteration and release planning. Perhaps you might choose to split your team into smaller teams of 10 people, who then each need a team leader that has more experience. More formality is also needed, and so are specialists. Having a team of just 40 programmers will not do in this case. 

Generally, the larger the team, the more complex the project and more formality is needed. Sapphire crystal types are almost unheard of and the documentation and planning needed for projects of this scope would be immense and probably impossible to control in the reald world. Larger projects also take longer, so iteration duration should be changed accordingly. Having 52 iterations in a year is not very practical and only creates more ceremonial work. The more members you have in your team, the more you need roles for people who specialize in just one thing. No one is a jack of all trades, but for small projects in the clear category, you can get away with not having any dedicated specialists assigned.

As for all agile methodologies you should follow the same agile principles in all of the crystal types by having constant customer feedback, frequent releases, time-boxed iterations, flexible teams and continuous testing. Read the [Agile Manifesto](https://agilemanifesto.org/) if you need a refresher. 