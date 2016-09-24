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

#### Test case execution:
The following resources are monitored while execution: 
  * Java heap memory: This is the memory space used to store Java objects. There is a garbage collector, so there can be leaks only when unused objects are unnecessarily referenced.
  * Native memory: This memory space is used by native code, and is made accessible to Java code via JNI (Java Native
Interface) calls. It requires explicit memory management by the developers as in programs written in non-garbage-collected languages such as C/C++, and thus could suffer from all well-known memory-related defects in those languages.
  * Binders: Binders provide an efficient inter-process communication mechanism in Android. Usage of binders requires
creation of global JNI references, and these references are made visible to the garbage collector. Unnecessarily keeping
these references could lead to leaking of other potentially large Java objects.
  * Threads. Threads are usually created to perform timeconsuming operations in a GUI application to maintain good responsiveness.  A sustained growth in the number of active threads in an application is an indication of software defects.

## Motivation
As of 2011, the android share of the smartphone market was over half which was double what it was in 2010. The android market exceeded 10 billion app downloads with a growth rate of 1 billion app downloads per month. The features of Android devices and the complexity of their software continue to grow rapidly. A few problems ever since the boom of the smartphone industry from a software engineering perspective are defects related to the limited resources, like memory, available on these devices. Improper management of resources, can lead to slowdowns, crashes, and negative user experience. But there does not exist a comprehensive and principled approach for testing for such leaks. Leaks in Android applications fortunately often follow a small number of behavioral patterns, which makes it possible to perform systematic, targeted, and effective generation of test cases to expose such leaks.

## Baseline Results for individual Android Applications:
  * APV: The application crashes with a large native memory footprint due to incorrect implementation in native memory reclamation. 
  * ConnectBot. SSH client ConnectBot has a defect related to leaking of event listener objects.

## Related Work
  * Memory leak detection and diagnosis: A body of work focussing on static analyses for memory leak detection. These
analyses typically require specification of resource management contracts/patterns, and it is an open question how
they can be effectively used for Android software.
  * Dynamic analyses of memory leaks, both for managed and unmanaged languages: These approaches have a shortcoming as to how can the leaking behavior be effectively triggered during testing.
  * Model-based GUI testing. Given a GUI model, test cases can be generated based on various coverage criteria. In these approaches the focus is typically on functional correctness and the coverage criteria reflect this. In contrast, this paper
is interested in non-functional properties, and the coverage categories we define explore specialized paths in the model
(with multiple repetitions of a neutral cycle) in order to target common leak patterns.
  * Random testing: For example, Hu and Neamtiu use the Monkey tool to randomly insert GUI events into a running Android application, and then analyze the execution log to detect faults. Random testing is highly unlikely to trigger
the repeated behavior needed to observe sustained growth in resource usage.
  * Testing and static checking for Android: Prior work has considered the use of concolic execution to generate sequences
of events for testing of Android applications, such as testing of exception-handling code when applications are accessing unreliable resources. As an alternative to testing, static checking can identify various defects including invalid thread accesses, energy-related defects, and security vulnerabilities.

## Future Work:
Important directions for future work, including additional coverage criteria; better diagnosis techniques (e.g., by correlating repeated behavior with heap growth); increased focus on analysis of native memory as well as analysis of specific
resources (e.g., database cursors, bitmaps); automated static or dynamic discovery/analysis of code that allocates and reclaims important resources; improved resource management through new software abstractions and patterns.

## Scope for improvement :

