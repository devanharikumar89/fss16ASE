# [Systematic Testing for Resource Leaks in Android Applications](http://web.cse.ohio-state.edu/presto/pubs/issre13.pdf)

## Key Words

#### Neutral Cycles :
Sequences of GUI events that should have a “neutral” effect and should not lead to increases in resource usage. Such sequences correspond to certain cycles in the GUI model. Through multiple traversals of a neutral cycle (e.g., rotating the screen multiple times; repeated switching between apps; repeatedly opening and closing a file), a test case aims to expose leaks. This approach directly targets several common leak patterns in Android applications.

#### GUI Model:
GUI models are directed graphs, with one node per activity, and with edges representing transitions triggered by GUI events. In addition to traditional events, the model should capture Android-specific events like pressing the home button. Several important GUI events are defined by the platform and not by the application:
  * ROTATE events. When the user rotates the screen, the current activity is recreated with a different orientation.
  * HOME events. When the user presses the hardware HOME button, the application is hidden.
  * POWER events. The hardware POWER button puts the device in a low-power state.
  * Sensor events. The platform can generate other events due to user actions. Aacceleration forces and rotational forces (triggered by the user) can be sensed by accelerometers, gravity sensors, gyroscopes, and rotational vector sensors [28]. Sensing a touch on the screen is also another user triggered sensor event.

#### Test Coverage Criteria:
. In general, for each state in the model, there is a transition representing an event. For each state, execute at least one test case that corresponds to a path and repeat the same transition. The motivation for this coverage is clear: resource usage should not increase when the neutral cycle transition is repeated even in large numbers.
  * Application-independent cycles: One category of cycles to be covered are those events defined by the platform, not by the application.
  * Cycles with BACK transitions: Cycles involving the hardware BACK button involve multiple activities, and present another target for coverage. This may expose leaks that depend on the interplay among several activities.
  * Application-specific neutral operations: Cycles involving pairs of operations that “neutralize” each other, like zooming in and zooming out.
  * Test case context: Context-sensitive variations of the coverage could also be defined, where different execution contexts for the neutral cycle need to be covered. Making such choices is very similar to defining different calling contexts for functions in code analysis and testing.

#### Intent : 

 
## Motivation
As of 2011, the android share of the smartphone market was over half which was double what it was in 2010. The android market exceeded 10 billion app downloads with a growth rate of 1 billion app downloads per month. The features of Android devices and the complexity of their software continue to grow rapidly. A few problems ever since the boom of the smartphone industry from a software engineering perspective are defects related to the limited resources, like memory, available on these devices. Improper management of resources, can lead to slowdowns, crashes, and negative user experience. But there does not exist a comprehensive and principled approach for testing for such leaks. Leaks in Android applications fortunately often follow a small number of behavioral patterns, which makes it possible to perform systematic, targeted, and effective generation of test cases to expose such leaks.

## Sampling Procedure 


## Related Work


## Future Work


## Scope for improvement :
