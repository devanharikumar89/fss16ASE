# Race Detection for Android Applications

## Key Words

#### Happens-before reasoning:
Based on the concurrency semantics, the authors define a happens-before relation over operations in execution traces. A naïve combination of rules for asynchronous procedure calls and lock-based synchronization introduces spurious happens-before orderings. Specifically, it induces an ordering between two asynchronous tasks running on the same thread if they use the same lock. This is a spurious ordering since locks cannot enforce an ordering among tasks running sequentially on the same thread. We overcome this difficulty by decomposing the relation into (1) a thread-local happens-before relation st which captures the ordering constraints between asynchronous tasks posted to the same thread and (2) an interthread happens-before relation mt which captures the ordering constraints among multiple threads.

#### Data Race :
A data race occurs if there are two accesses to the same memory location, with at least one being a write, such that
there is no happens-before ordering between them

#### DROIDRACER:
We have implemented our race detection algorithm in a tool called D ROID R ACER . D ROID R ACER provides a framework that
generates UI events to systematically test an Android application. It runs unmodified binaries on an instrumented Dalvik VM and instrumented Android libraries. A run of the application produces an execution trace, which is analyzed offline for data races by computing the happens-before relation. The control flow between different procedures of an Android application is managed to a large extent by the Android runtime through callbacks. D ROID R ACER uses a model of the Android runtime environment to reduce false positives that would be reported otherwise. Further, D ROID R ACER assists in debugging the data races by classifying them based on criteria such as whether one involves multiple threads posting to the same thread or two co-enabled events executing in an interleaved manner.

#### Execution Trace:
Any task in the execution scenario of an android application can be divided into a sequence of more transparent and concurrency-relevant low level operations called execution traces. They are used in this paper to model the flow and execution of different android applications.

## Motivation
The paper speaks about a motivating example of an android application that is as ubiquitous as a media player. The paper mentions in detail the classes and threads that are involved in downloading a media from the web and playing it. Even this simple execution scenario for the music player application involves four threads running in two different processes. Moreover, much of the complex control flow and inter-thread communication in this example is managed by the Android runtime itself and is opaque to the developer. Nevertheless, the developer must understand the semantics clearly to avoid concurrency bugs. 

## Baseline Results:
  * APV: The application crashes with a large native memory footprint due to incorrect implementation in native memory reclamation. 
  * ConnectBot. SSH client ConnectBot has a defect related to leaking of event listener objects.
  * KeePassDroid. When the application is first launched, it displays a list of database files in FileSelectActivity for the user to choose. When a database file is selected, a query is launched to retrieve the information in the file, and the result can be accessed through a Cursor object. The Cursor is remembered in a container so that it can be synchronized with the activity. The Cursor object is automatically cleaned up when its managing activity is destroyed. However, when we keep the same instance of FileSelectActivity alive, and come back to the selection list to select database files repeatedly, multiple Cursor objects would be saved in FileSelectActivity.
  * K9. In K9, a popular email client, a leak was discovered when rotating the screen after an email message is selected
for display. Since it crashes after only a few repetitions of the ROTATE neutral cycle, this is an example of a leak that can
be easily observed and thus cause negative user perception of the application.

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
The paper doesn't consider the user driven sensor inputs that generates events. This can make a bulk of the faults and is a big shortcoming of the paper.
