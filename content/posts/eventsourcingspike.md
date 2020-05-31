Title: Event Sourcing Spike
Date: 2020-05-25
Category: Project
Tags: c#, ddd, event-sourcing, console, microservices, event store
Slug: event-sourcing-spike
Author: Thomas Brunbjerg
Summary: Spike for testing a .NET implementation of Event Sourcing and EventStore using DDD architecture
featured_image: img/eventsourcingspike_01.png
repository: https://github.com/ThomB93/EventSourcingSpike

Event Sourcing is an alternative approach to data persistence that leverages the use of events to capture past actions in the system as a way to store information. The source of these events are the system(s) in which Event Sourcing is being applied. Instead of storing tables of data, as in traditional relational databases, data is stored using 'event streams', with each stream corresponding to a a business entity. 