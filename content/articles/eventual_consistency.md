Title: Eventual Consistency
Date: 2020-05-30
Category: Article
Tags: eventual, consistency, database, distributed systems
Slug: eventual-consistency
Author: Thomas Brunbjerg
Summary: 
report: article

Eventual Consistency describes the notion that for a given distributed computing system, updates to one server will *eventually* be propagated to all servers in the network. A user may send a request to one server and receive a response, before the server has received the latest update, making the respones contain stale data. Many modern NoSQL systems can be said to be Eventually Consistent, as the need for constant availability trumphs the need for always consistent data. In addition, most of these systems are distribued across a multitude of servers, making the prospect of consistency difficult to achieve - see the [CAP Theorem]({filename}/articles/cap_theorem.md) as to why this is the case.

In short, the concept can be summed up as follows:
*"If no additional updates are made to a given data item, all reads to that item will eventually return the same value."*

It takes time to replicate data across servers, thus making some nodes in the network contain stale data for a short period of time. Shortening this 'time to update' will make the system appear more consistent, but it can never appear to have reached a fully consistent state. To achieve low-latency reads, as is the case in most modern systems, a trade-off between availabiltiy and consistency must be made. High volumes of internet traffic creates a huge load on databases, thus creating a need for scalability. 

[![small]({static}/img/article/eventualconsistency.png)]({static}/img/article/eventualconsistency.png)

Whether a system can tolerate stale data depends on the domain. Banking systems often cannot deal with data that is out of date. Your bank balance must always reflect its sum of transactions and in the correct order. These systems are said to be heavily consistent and are based on the ACID (Atomicity, Consistency, Isolation, Durability) principles. A good example of a system that does tolerate stale data is Google Docs. When multiple users are working on the same document, then it does not matter whether each user receives a fully consistent copy of the document being edited - eventually a convergence between the servers will have been reached and all users will have the same document in front of them.

It might seem strange that many large distributed systems today can even function with weak consistency models. In fact these systems do *appear* strongly consisent most of the time and software architects can design these systems in such a way that inconsistencies are kept to a minimum, even when data is spread between hundreds or even thousands of servers. Of course having the system be 'always online' and instantly react to all user request, a better user experience is provided. In a competitive app market the user experience makes or breaks whether an app will be a success. Facebook timelines are also served to be eventually consistent. If not, some users would receive a message saying something like "Sorry, your timeline is not yet up to date. Please wait before posting until all updates have been received". Many users would just simply using the service at that point. 

While eventual consistency might seem like a yes/no guarantee, in reality it exists on a spectrum between weak and strong eventual consistency. In the weaker end you have a system that does not make any distinctions between writes and cannot ensure that data is ever in any consistenet state. In the stronger end you have systems that might guarantee that two or more servers who receives the same writes (unordered) will be in the same state. In addition you may want a stronger consistency in some parts of the system, while in other parts serving state data might be more tolerable.

[![medium]({static}/img/article/eventualcomic.jpg)]({static}/img/article/eventualcomic.jpg)