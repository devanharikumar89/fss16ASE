# [Semantically Rich Application-Centric Security in Android](http://www.enck.org/pubs/acsac09.pdf)

## Key Words

#### Application (Security) Policies :
Policies specified as part of Android framework that takes care of security in the system. They can govern a myriad of areas like what applications can be installed, which other applications or user can have access to what data inside another app, to whom to provide access to ones own interface and how to continue monitor fair and secure usage of the interface.

#### Secure Application INTeraction (Saint) framework:
It extends the existing Android security architecture with policies for applications that address some key application requirements like:
  * Control to whom permissions to use its interface can be granted,
  * Control how its interfaces can be used by applications that were permitted to use them, and 
  * Determine at run-time, what other interfaces can they use.


#### Policy enforcements by SAINT framework : 
  * Install-Time: An application declaring permission P defines the conditions under which P is granted to other applications at install-time. Conceptually, the an application requesting the permission P can be installed only if the policy for acquiring P is satisfied.
  * Run-Time: Any interaction between software components within android framework involves a caller application and a callee application. The interaction is allowed to continue only if all policies supplied by both the caller and callee are satisfied.
  * Administrative: An administrative policy dictates how policy itself can be changed.
  * Operational: This section defines policies that detect when Saint renders an application inefficient, faulty, or inoperable, so that by restricting access to interfaces, Saint doesn't hamper utility. Past security measures that have prevented application behavior in an opaque and ambiguous way have not fared well

#### JUnit : 

 
## Motivation
Smartphones are now ubiquitous even though they are new systems whose security infrastructure is largely underdeveloped.
The existing Android operating system needs to be augmented with a framework to meet the security requirements of android applications.
Applications statically identify the permissions that govern the rights to their data and interfaces at installation time.
This means that the application/developer has limited ability thereafter to govern to whom those rights are given or how they are later exercised.
Thus, a necessary utility needs to be developed for applications to assert and control the security decisions on the platform.

## Baseline results

## Sampling Procedure 


## Related Work



## Scope for improvement :
