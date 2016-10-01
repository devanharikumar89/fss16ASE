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
  DROIDRACER was applied on 10 open-source applications and 5 proprietary applications from different categories like entertainment, communication, personalization, and social networking. These include popular, feature-rich applications like Twitter and Facebook with more than hundred million downloads each. Some of the applications exhibited complex concurrent behavior by spawning many threads, starting Service components, and triggering Broadcast Intents, even before D ROID R ACER triggered the first UI event on those applications. For such applications, we triggered sequences of 1–3 events only. For each application, D ROID R ACER found tests which manifested one or more races. This shows that data races are prevalent in Android applications.

## Related Work
  * There are some tools that target specific types of concurrency bugs in Android. Dimmunix is a tool to detect and recover from deadlocks. There are tools that check Android applications against specific thread usage policies; e.g., Android’s StrictMode tool dynamically checks that the UI thread does not perform I/O or other time-consuming operations, Zhang et al.  statically check that only the UI thread accesses UI objects.
  * The concurrency model exposed by Android is different compared to the models explored in the literature in the context of race detection. There is of course a large body of work on static and dynamic race detection techniques for multi-threaded programs, e.g., based on locksets or happens-before relations or their effective combinations. However, these algorithms do not consider asynchronous calls, and either do not scale or produce many false positives, if asynchronous calls are simulated through additional threads.
  * Recent work on race detection for client-side web applications considers the happens-before relation for single threaded event-driven programs and framework-specific rules to capture the semantics of browsers and JavaScript. However, their analysis is not immediately applicable to Android because there is additional interference through multi-threading

## Future Work:
In the authors words, "Android is an expressive programming environment, and our formalization does not capture all its features. For example, we have not formalized its handling of inter-process communication (except IPCs relating to lifecycle events). D ROID R ACER only generates UI events but not intents in the testing phase. Modeling and implementing these additional features are left for future work. We also wish to investigate how to provide better debugging support, e.g., by analyzing the races that fall in the unknown category.

## Scope for improvement :
If there are multiple races belonging to the same category on the same memory location, D ROID R ACER reports any one of them randomly. But if DROIDRACER is to be used as a tool for Concurrency Semantics, all race conditons have to be exhaustively listed.
The manual inspection to distinguish between true and false positives. (1) For multi-threaded and cross-posted races,stall certain threads using breakpoints, giving others the opportunity to progress or to enforce a different ordering of asynchronous procedure calls. (2) For co-enabled races, change the order of triggering events. (3) For delayed races, alter delay associated with asynchronous posts. The paper does not talk about how these variations are achieved.
