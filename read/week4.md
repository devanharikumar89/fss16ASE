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
A fictitious PersonalShopper smart-phone shopping application was chosen for explaining the drawbacks of the current Android Security Framework. This application was expected to enforce the following:
* use only trusted payment services.
* restricts the use of services to safe networks.
* works only with approved versions of certain applications.
* ensure transaction information is not leaked to the phone's ledger application.
* allow other applications to place security restrictions on PersonalShopper.

## Related Work
Security Permissions to applications can be validated during install time or during run-time. Systems for run-time validation of Security Permissions are not very developed. Frameworks which validate permissions during install time are:
* Kirin - enforces install policies that validate if the permissions requested by applications are consistent with the System policies.
* Open Mobile Terminal Platform - determines an application's access rights based on its origin.
* Symbian framework prevents unsigned applications from accessing 'protected' interfaces.
* MIDP 2.0 Security Framework relies on the Mobile Information Device Profile implementor in giving access.

## Future Work
The idea is to convert Saint from a research system to a viable framework for Android Devices. In order to do that more applications and the protection policies they require needs to be integrated into the system. The Saint policies to protect the phone system services and the cellular network needs to be extended too.

## Scope for improvement :
Even though the paper demonstrates a new Framework for addressing the security limitations in Android devices, it fails to depict the impact of this new Framework. The paper does not mention any experiments conducted on this new framework. It would have been nice to test for security issues in different applications with the existing framework and then compare the results with Saint.
