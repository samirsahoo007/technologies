# Creating New Gradle Builds
❯ cd basic-demo
❯ gradle init                   # Starting a Gradle Daemon (subsequent builds will be faster)
                                # gradle init --dsl kotlin      # If you want to use the Kotlin DSL
```
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


