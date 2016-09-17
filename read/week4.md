# [Reverse Engineering Finite State Machines from Rich Internet Applications](http://ieeexplore.ieee.org/document/4656395/)

## Key Words

####  RIA : Rich Internet Applications
New generation of web applications offering greater usability and  interactivity than traditional ones, while at the same time suffering from a serious problem of lack of suitable software models to fit into.

#### AJAX: Asynchronous Javascript and XML 
Indicates an approach for developing RIA's using a combination of web technologies that allow a browser to communicate with the server without refreshing the current page. 

#### XHR : XMLHttpRequest  
Allows asynchronous retrieval of arbitrary data from the server. It has produced an important shift in the internet default Request/Response paradigm


#### DOM : Document Object Model
DOM is a standard application program interface (API) for HTML and XML documents that defines the logical structure of documents and the way a document can be accessed and manipulated.

## Motivation
The motivation of this paper stems from the differences between RIA and traditional web applications. At the presentation layer traditional web applications are form based softwares, whereas RIA's have complex asynchronous mechanisms that help them contact the server without refreshing the whole page, thanks to the AJAX engine. Such features in RIA make it difficult to fit them into a software model. This paper aims at reverse engineering one such application into an FSM.

## Sampling Procedure 
The subject of the experiment was an Ajax-based RIA named FilmDB that provides registered users with several functionalities for data management of a personal movie archive. The server side of this application is implemented by 99 PHP server pages (624 kBytes) that generate client pages containing several scripts (coded in Javascript) implementing a complex user
interface. Moreover, FilmDB interacts with other server side resources by exploiting Ajax (XHR) requests.

## Informative Visualizations

Class Diagram

![class diagram](https://github.com/arjunaugustine/fss16ASE/blob/master/read/pics/Screen%20Shot%202016-09-16%20at%2010.28.10%20PM.png)

Activity Diagram

![activity diagram](https://github.com/arjunaugustine/fss16ASE/blob/master/read/pics/Screen%20Shot%202016-09-16%20at%2010.28.31%20PM.png)

Component Diagram

![component diagram](https://github.com/arjunaugustine/fss16ASE/blob/master/read/pics/Screen%20Shot%202016-09-16%20at%2010.28.44%20PM.png)

## Future Work 
Future work includes extending the experimentation with further case-studies in order to assess the scalability of the approach. It involves addressing the adequacy of the proposed model for supporting maintenance and testing activity involving RIA's. 

## Scope for improvement :


