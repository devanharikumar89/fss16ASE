# Using GUI Ripping for Automated Testing of Android Applications by Domenico Amalfitano, Anna Rita Fasolina, Porfirio Tramontana, and Salvatore De Carmine, Atif M. Memon
Proceedings of the 27th IEEE/ACM International Conference on Automated Software Engineering

## Key Words

#### GUI Ripping :
GUI Ripping is a dynamic process in which the software's GUI is automatically traversed by opening all its windows and extracting all their widgets (GUI objects), properties, and values. The extracted information is then verified by the test designer and used to automatically generate test cases. [Ripping](http://www.cs.umd.edu/~atif/pubs/MemonWCRE2003-abstract.html)
#### Monkey :
A non commercial random stress and crash testing tool for Android GUI's. It generates pseudo-random streams of user events such as clicks, touches, or gestures, as well as a number of system-level events. You can use the Monkey to stress-test applications that you are developing, in a random yet repeatable manner. [Monkey ](https://developer.android.com/studio/test/monkey.html)

#### GUI Exploration Criterion : 
The GUI exploration decides whether GUI exploration using a particular input is to be continued or not. Certain metrics may help in making this decision - ensure the depth of resultant GUI tree is less than a specified maximum, or if the resultant state is equivalent to an already evaluated state.

#### Activity Component : 
An activity represents a single screen with a user interface. For example, an email app might have one activity that shows a list of new emails, another activity to compose an email, and another activity for reading emails. Although the activities work together to form a cohesive user experience in the email app, each one is independent of the others. As such, a different app can start any one of these activities (if the email app allows it). [Activity](https://developer.android.com/guide/components/fundamentals.html)

## Baseline results
Monkey execution for __4.46 hours__ firing __45,000 events__ with the default value of event type statistical distribution finding __3 crashes__ reaching __25.27 % LOC coverage__.

## Sampling Procedure 
Monkey - Chosen because that was the only non-commercial automated android testing tool "to the best of author's knowledge"
Wordpress - Opensource android blogging software with broad user community with an issue tracking system

## Statistical Tests
Implemented the AndroidRipper using the Robotium Framework and by the Android Instrumentation class.
Metrics Used :

   * Defect Detection Effectiveness
   * Code Coverage Metric
   * Time(Resource) spent

## Scope for improvement :
 Even though the AndroidRipper has exhibited a tremendous improvement over the Monkey tool, it appears that the comparison is done solely for one software. The paper does not compare AndroidRipper with any other software nor does it provide an analysis of any other android app (other than Wordpress). So there is evidently a lack of data to support the claim that AndroidRipper is the best tool.
 
 Also, another scope for improvement would be augmenting the tool's capabilities to find logical(Semantic) bugs as well.
 
 ## Motivation
 As of 2011, the android share of the smartphone market was over 52.5% which was double what it was in 2010. The android market exceeded 10 billion app downloads with a growth rate of 1 billion app downloads per month. A few problems ever since the boom of the smartphone industry from a software engineering perspective are 
 
    * lack of cost-effective approaches for development and
    * defining suitable techniques and tools for testing
