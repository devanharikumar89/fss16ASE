# [Automating GUI testing for Android applications](http://www.cs.ucr.edu/~neamtiu/pubs/ast11hu.pdf)

## Key Words

#### Software reliability :
It is the probablity of failure free software operation for a specified period of time in a specified environment. 
#### Dalvik VM:
An optimized android specific java virtual machine. 
#### Broadcast receiver : 
A component that listens and reacts to broadcast announcements, like an email client receiving notifications about low battery.
#### JUnit : 
A testing framework for java applications integrated in the android development environment.
 
## Motivation
Android is a popular mobile platform with more than 50% market share and reliability of the applications on the platform are getting increasingly important. Owing to the GUI oriented application construction paradigm of android and its novelty, many existing andriod software correctness issues fall outside the scope of traditional verification techniques. The study aims to automate andriod testing so as to detect more bugs and increase the quality of developed software.

## Baseline results
The technique tries to detect bugs classified into three broad categories: activity bugs, event bugs, and type errors. It detected all 8 previously reported activity bugs and 3 new ones. It also detected 18/21 old event bugs and 6 new ones, and attribute the three missing older bugs to spurious reporting of older bugs. It detected all 4 old type errors, but no new ones.

## Sampling Procedure 
The following criteria were taken into account while sampling the apps:
  * Popularity
  * Long lifetime
  * Detailed bug history
  * Open-source source code
  * High download counts
  * High bug category coverage

## Related Work
  * Android verification: Kirin, a logic based tool for android that ensures permissions needed by a certain andrioid application are met by a global safety invariance. Saint enforces OS level data for security. Taintdroid: checks data misuse during runtime for an android application.
  * Gui Testing: Kervinen et. al.: model tests mobile applications running on symbian platform. Guitar: Gui testing framework for java and windows applications.
  * Android Bug Studies: Maji et. al. failure characterization study found that defect density tends to be lowest in the OS, higher in the middleware, and highest in core applications.


## Scope for improvement :
Though the technique demonstrates considerable improvement over Monkey tool, the paper doesnot involve any associated data like code coverage, that would help identify the shortcomings and better the results. Also, the technique might actually be using considerably more resources like computing power and time to get to the results that it got. The paper should add these data to the results so that their results are more solid.
