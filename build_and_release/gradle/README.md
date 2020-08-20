# Creating New Gradle Builds
❯ cd basic-demo
❯ gradle init                   # Starting a Gradle Daemon (subsequent builds will be faster)
                                # gradle init --dsl kotlin      # If you want to use the Kotlin DSL
```
❯ tree basic-demo

├── build.gradle                                        # Gradle build script for configuring the current project
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar                          # Gradle Wrapper executable JAR
│       └── gradle-wrapper.properties                   # Gradle Wrapper configuration properties
├── gradlew                                             # Gradle Wrapper script for Unix-based systems
├── gradlew.bat                                         # Gradle Wrapper script for Windows
└── settings.gradle                                     # Gradle settings script for configuring the Gradle build
```

## Create a task to copy file from src to dest
Add the following to build.gradle
```
task copy(type: Copy, group: "Custom", description: "Copies sources to the dest directory") {
    from "src"
    into "dest"
}
```
❯ ./gradlew copy                                        # dest directory should have got created with file which was in src directory

## Apply a plugin and create a zip file
Add the following to build.gradle

```
task zip(type: Zip, group: "Archive", description: "Archives sources in a zip file") {
    from "src"  
    archiveFileName = "basic-demo-1.0.zip"
}
```

❯ ./gradlew zip

❯ ./gradlew tasks                                       # Discover available tasks in build.gradle like zip, copy etc

❯ ./gradlew properties                                  # Discover available properties

# Building Java Applications

```
$ cd demo
$ gradle init
> Task :wrapper

Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Swift
Enter selection (default: Java) [1..5]

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2]

Select test framework:
  1: JUnit 4
  2: TestNG
  3: Spock
  4: JUnit Jupiter
Enter selection (default: JUnit 4) [1..4]

Project name (default: demo):

Source package (default: demo):


> Task :init
Get more help with your project: https://docs.gradle.org/5.4.1/userguide/tutorial_java_projects.html

BUILD SUCCESSFUL
2 actionable tasks: 2 executed

❯ tree demo

├── build.gradle
├── gradle    
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    ├── main
    │   ├── java  
    │   │   └── demo
    │   │       └── App.java
    │   └── resources
    └── test      
        ├── java
        │   └── demo
        │       └── AppTest.java
        └── resources
```

Now check
```
settings.gradle
build.gradle
src/main/java/demo/App.java
src/test/java/demo/AppTest.java
```

❯ ./gradlew build					# Execute the build

❯ ./gradlew tasks					# Run the application


