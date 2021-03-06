# How to get the API Token for Jenkins

Since Jenkins 2.129 the API token configuration has changed:
You can now have multiple tokens and name them. They can be revoked individually.

* Log in to Jenkins.

* Click you name (upper-right corner).

* Click Configure (left-side menu).

* Use "Add new Token" button to generate a new one then name it.

* You must copy the token when you generate it as you cannot view the token afterwards.

* Revoke old tokens when no longer needed.

# Difference between jenkins job and pipeline

* Jenkins Job and Jenkins Pipeline are basically the same. In a pipeline you define the steps of your job as groovy code (actually it is CPS https://github.com/jenkinsci/workflow-cps-plugin, but that should in general just be a custom groovy interpreter).



* The point, that is making pipelines "better", form my perspective, is, that you can add those in so-called Jenkinsfiles alongside your code. So you have your build job versionized alongside your application code.

# Configuring JAVA_HOME in Jenkins

1. Open the Jenkins dashboard.

2. Go to Manage Jenkins.

3. Go to Global Tool Configuration to configure tools, their locations, and automatic installers.

4. Go to the JDK section.

5. Give the Name and tick the Install automatically option; provide details for the Oracle account to download JDK successfully.

6. You can give a logical name such as JDK 1.7 or JDK 1.8 to identify the correct version while configuring a build job.

7. You can add multiple JDKs based on the version, so if different applications require different JDKs then the scenario can be managed easily by adding JDK in Jenkins:


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/java_home_setup.png)


# Configuring JDK in Jenkins

Below are the steps to be followed in order to configure the JDK in Jenkins :

1. Deploy the Jenkins.war into the tomcat server and start the server.

2. From the home page, click on the link Manage Jenkins and click on Configure System as shown below :


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/configuring-jdk-1.png)


3. From the next page, click on "Add JDK". The easiest way to configure JDK is to provide a name and path of the java installation directory. (Consider the same path used for JAVA_HOME). In the below screenshot JDK 6 and JDK 7 has been configured,

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/configuring-jdk-2.png)

4. JDK can also be installed by intimating Jenkins to do the task. The check box install automatically needs to be checked in this case. Jenkins will download and installs the specified version of the JDK into the tools directory of the Jenkins home directory.


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/configuring-jdk-3.png)



