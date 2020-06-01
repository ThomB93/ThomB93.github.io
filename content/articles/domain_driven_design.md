Title: Domain Driven Design (DDD)
Date: 2020-05-30
Category: Article
Tags: domain, driven, design, microservices, ddd
Slug: domaindrivendesign
Author: Thomas Brunbjerg
Summary: Describes the ideas behind Domain Driven Design and its use in a Microservice architecture
report: article

Domain-Driven Design was first introduced by Eric Evans in his book of the same name from 2004, in which he outlines the basic principles of the idea. In short, DDD attempts to help developers and non-developers make sense of complex projects by making the domain, and the domain-specific language the core of the design. While this approach is not new in itself, the terms used by Evans to help describe the design is. When the domain and its language becomes the central focus point, developing and maintaining software becomes easier and more manageable. 

The concepts and relationships between the different parts of the domain are captured in 'domain models'. These models can then be broken further down into 'bounded contexts' - logical boundaries that encapsulate different sub-domains. Sadly, there is (yet) no formal definition of when a certain part of the domain should be considered a bounded context - it depends on the individual domain. Some contexts will appear more straightforward than others. Building a single model that unifies the entire domain is hard if not impossible. So to solve this problem, each bounded context should be seen as its own 'unified model'. Its smaller scale means that unifying all its internal domain concepts is feasible. Some bounded contexts may overlap if they share similar concepts - in this case, special care should be taken to avoid mixing up similar terms whose meaning can change drastically in different contexts. The term 'Product' may be interpreted in many different ways depending on the context in which it is expressed. 

When attempting to gain an understanding of DDD, it is paramount to know the concepts used. Some of these concepts can be mapped to UML equivalents, but their definitions are less strict and are up for interpretation by the developers.

The diagram below attemps to give an overview of how the DDD concepts are interconnected and related. Some of these correspond to types, while others represent a pattern, such as Factories and Repositories. 

[![small]({static}/img/article/ddd_overview.png)]({static}/img/article/ddd_overview.png)

**Entity:** A domain object that is distinguished by its identity. It is not defined by its attributes but as an individual object. These are the most prevalent objects in DDD.

**Value Object:** An immutable object that has no domain-specific identity. You can view this as the opposite of the Entity object. Entities may consist of value objects, but each value object does not hold an identity in itself.

**Aggregate:** A cluster or group of entities and value objects that are associated. Each aggregate has a 'root Entity' called an Aggregate Root, which functions as an access point. None of its members may be referenced outside the root. A bounded context may contain many or just one aggregate. 

**Domain Events:** Domain objects that can be mapped to something that happens in the domain. Used when you want other parts of the domain to be aware of and react to past events, which is the case in most systems. 

**Ubiquitous Language:** The use of a shared language between all participants of the project. Words may mean different things in different contexts, so establishing a shared understanding of how each word should be interpreted is important. Also, the actual code of the software should reflect this shared understanding by using variable names, etc. that match the context in which they are used. All this helps decrease the risk of any misunderstanding between the project members. The UL may also serve as a form of documentation as the project progresses. 

Other terms are used in DDD, but these are the most important to know about. In practice, each of the domain objects would correspond to a class, but with varying implementations. Let's say you have the concept of a 'Car' in your domain. The car itself would be an aggregate, that contains individual parts (entities). Each entity may then contain different value objects that describe its attributes such as color, size, and material. Each part of the car has its own identity, but the value object 'Color' does not, as it merely describes the information of the entity. It is possible to change the distinction so that the entities become value objects, but it depends on the context in which they exist. 

[![small]({static}/img/article/ddd_boundedcontext.png)]({static}/img/article/ddd_boundedcontext.png)

With the rise of Microservice Architecture, the need for and relevance of DDD has increased, since it provides a good foundation of creating microservices. Each bounded context can (almost) be directly mapped to each individual Microservice, making the implementation of this otherwise complex architecture style easier to handle. The word 'bounded' refers to the strict boundaries that exist in the context being encapsulated. Of course, you can't have different parts of the same system not communicate, so each bounded context, or Microservice, also share relationships. Another way of encapsulation are modules, which simply structure the domain objects in different namespaces. 

However, as mentioned, DDD does not contain a formal definition of its patterns and so its practical use in projects of a higher scope can be put into question. When a project reaches a high scope, the benefits may come at a high cost. It should only be applied to domains in which the domain language can help foster better communication and help in making sense of complex information. 

The key principles of DDD can be summed up as follows:

* Close collaboration between the business and technical people is highly important, not only when determining the requirements, but throughout the entire project lifecycle. 

* The focus should always be on the core domain(s). These are the bread and butter of the application and will provide the most value.

* The software should closely reflect the real world - at least to a degree in which it makes sense.

* Sub-domains should be split into bounded contexts with clearly defined boundaries. Communication between the sub-domains should be strictly structured around the aggregate roots contained within.

* The aggregates, entities and value objects should be clearly defined within the domain and be implemented using the ubiquitous language in mind. 



