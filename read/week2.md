# [Automating GUI testing for Android applications](http://www.cs.ucr.edu/~neamtiu/pubs/ast11hu.pdf)

## Key Words

#### Ripping :
Ripping 
#### Monkey :
A non commercial 
#### GUI : 
The GUI 

#### Activity Component : 
An activity
 
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

## Statistical Tests


## Scope for improvement :
Though the technique demonstrates considerable improvement over Monkey tool, the paper doesnot involve any associated data like code coverage, that would help identify the shortcomings and better the results.
