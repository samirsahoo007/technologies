
# GitHub Pull Request Builder Plugin

This Jenkins plugin builds pull requests from GitHub and will report the results directly to the pull request via
the [GitHub Commit Status API](http://developer.github.com/v3/repos/statuses/)

When a new pull request is opened in the project and the author of the pull
request isn't whitelisted, builder will ask ``Can one of the
admins verify this patch?``. One of the admins can comment ``ok to test``
to accept this pull request for testing, ``test this please`` for one time
test run and ``add to whitelist`` to add the author to the whitelist.

If an author of a pull request is whitelisted, adding a new pull
request or new commit to an existing pull request will start a new
build.

A new build can also be started with a comment: ``retest this please``.

You can extend the standard build comment message on GitHub
creating a comment file from shell console or any other 
jenkins plugin. Contents of that file will be added to the comment on GitHub. 
This is useful for posting some build dependent urls for users without 
access to the jenkins UI console.

Jobs can be configured to only build if a matching comment is added to a pull request.  For instance, if you have two job you want to run against a pull request,
a smoke test job and a full test job, you can configure the full test job to only run if someone adds the comment ``full test please`` on the pull request.

For more details, see https://wiki.jenkins-ci.org/display/JENKINS/GitHub+pull+request+builder+plugin

## GitHub Pull Request Builder Setup

### Install the Plugin

The first step is to install the plugin in Jenkins.  If you’re not familiar with installing plugins in Jenkins, navigate to Manage Jenkins -> Manage Plugins and open the “Available” tab.  Start typing “Github Pull Request Builder” into the filter bar until you see it in the results section.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_1.png)

the ghprb plugin

Note that, as of this writing (October 2018) the plugin still displays a security warning.  Earlier versions of ghprb were storing objects in a build.xml which contained your GitHub credentials.  Users with access to the servers file system could then potentially obtain said credentials.  However, this issue was fixed in version 1.40.0, so if you are installing the plugin for the first time, this is not something you need to worry about.

### Configuration

Now we need to configure ghprb.  In Manage Jenkins -> Configure System, there should now be a section entitled “GitHub Pull Request Builder”.  The “GitHub Server API URL” field should always be https://api.github.com, unless your company has its own “Enterprise GitHub” solution deployed on-site, in which case you will need to use whatever the url for your instance is.  We don’t want to override our Jenkins url, and we don’t need to worry about the “Shared Secret” field as it will be auto-populated by our GitHub credentials.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_2.png)

					ghprb configuration section

If you already have GitHub credentials stored in Jenkins, they will be available in the “Credentials” dropdown.  If you don’t, or if you want to add a new credential, you can see there is a helpful “Add” button right next to the credentials dropdown.  In the popup, enter the username and password of the GitHub account you want to associate to the builder.  You can leave the “Id” and “Description” fields blank, as they will be auto-generated.  Optionally, you can restrict the credentials to the GitHub “Domain”, but it will be fine if you leave them as global.  Obviously, they will only work for GitHub.

After setting up the user credentials, we can use the “Test Credentials” section to add a comment to a pull request (Yay).

 
![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_4.png)

							makin’ a poast

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_4_5.png)

							my poast is success!

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/webhook.jpg)

### Setup GitHub Webhook

After we save, the ghprb will generate an endpoint at https://<your-jenkins>/ghprbhook/ which we can send info to via webhook.  Navigate to the repo in question, and under the “Settings” tab, select “Webhooks”.  Add the endpoint URL to the “Payload URL” field.  We also need to select which events trigger the webhook.  For our purposes, we only need to check “Pull Requests” (because we are building pull requests), and “Issue Comments” (for ghprb status magics).


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_4_6_1.png)

							makin’ them webhooks


##  The Jenkins Job

Finally, we can make our job.  Create a New Item and make it a “Freestyle” project.

Under “General” set the project as a GitHub project and put the url of the repo in the text box.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_5.png)

							yup

Under “Source Code Management”, we will select “Git” (suprise), and then enter the credentials we created earlier.  In the “Branch Specifier” field the default branch to build is ``*/master.  Set it to blank to allow builds against any branch (like develop for example).  Under the “Advanced” section, make sure the “Refspec” field is set to +refs/pull/*:refs/remotes/origin/pr/*.``


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/Screen-Shot-2018-10-23-at-11.19.16-PM.png)

						the source code settings


Under “Build Triggers”, select the ghprb and use the same API credentials we created earlier (if you’re starting from scratch it should be the only one available in the dropdown).  You will also need to go into the “Advanced” fields and select the checkbox next to “Build every pull request automatically without asking”, otherwise the tests won’t run automatically when a pr is created.


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_7.png)

						build triggers
 

Obviously, in real life we want to actually do something when the build is triggered.  For this example, I’m just going to execute a bash command that prints “hello test”.


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_8.png)

						important build step

## GitHub Branch Rule

Once we save our job configuration, we have everything we need to run tests (or in this case, print statements) against our pull requests.  Go ahead and make one, you should see something like this.


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_9_1.png)

						success

Clicking on the “Details” link will redirect you the Console Output on the Jenkins box, where you can in fact confirm that “hello tests” was printed.

The last step is to add a rule to the branch to prevent merges on failing tests.  If we go into the repos Settings -> Branches page and select “Add Rule”, we can require that the tests pass before the PR can be merged.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/pic_9.png)

						NO MERGING!

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/Screen-Shot-2018-10-23-at-6.57.34-PM.png)

						a failing unit tests

Administrators can still override the rule, but GitHub makes you feel really bad about doing it (you should feel bad).


# 5 Simple tips for boosting your Jenkins performance

## Tip 1: Minimize the amount of builds on the master node

The master node is where the application is actually running, this is the brain of your Jenkins and, unlike a slave, it is not replaceable. So, you want to make your Jenkins master as "free" from work as  you can, leaving the CPU and memory to be used for scheduling and triggering builds on slaves only. In order to do so, you can restrict your jobs to a node label, for example: 


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/restrictToLabel-2.png)

```
stage("stage 1"){
    node("ParallelModuleBuild"){
        sh "echo \"Hello ${params.NAME}\" "
    }
}
```

In those cases, the job and node block will only run on slaves labeled with ParallelModuleBuild.

## Tip 2: Do not keep too much build history

When you configure a job, you can define how many of its builds, or for how long they, will be left on the filesystem before getting deleted. This feature, called Discard Old Builds, becomes very important when you trigger many builds of that job in a short time. I have encountered cases where the history limit was too high, meaning too many builds were kept on the filesystem. In such cases, Jenkins needed to load many old builds – for example, to display them in the history widget, – and performed very slowly, especially when trying to open those job pages. Therefore, I recommend limiting the amount of builds you keep to a reasonable number.


![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/discardOldBuilds.png)

## Tip 3: Clear old Jenkins data

As you probably know, Jenkins keeps the jobs and builds data on the filesystem. When you perform an action, like upgrading your core, installing or updating a plugin, the data format might change. In that case, Jenkins keeps the old data format on the file system, and loads the new format to the memory. It is very useful if you need to rollback your upgrade, but there can be cases where there is too much data that gets loaded to the memory. High memory consumption can be expressed in slow UI responsiveness and even OutOfMemory errors. To avoid such cases, it is best to open the old data management page (http://JenkinsUrl/administrativeMonitor/OldData/manage), verify that the data is not needed, and clear it.

![alt text](https://github.com/samirsahoo007/technologies/blob/master/jenkins/images/manageOldData.png)

## Tip 4: Define the right heap size

This tip is relevant to any Java application. A lot of the modern Java applications get started with a maximum heap size configuration. When defining the heap size, there is a very important JVM feature you should know. This feature is called UseCompressedOops, and it works on 64bit platforms, which most of us use. What it does, is to shrink the object’s pointer from 64bit to 32bit, thus saving a lot of memory. By default, this flag is enabled on heaps with sizes up to 32GB (actually a little less), and stops working on larger heaps. In order to compensate the lost space, the heap should be increased to 48GB(!). So, when defining heap size, it is best to stay below 32GB. In order to check if the flag is on, you can use the following command (jinfo comes with the JDK):

```
jinfo -flag UseCompressedOops <pid>
```

## Tip 5: Tune the garbage collector

The garbage collector is an automatic memory management process.

Its main goal is to identify unused objects in the heap and release the memory that they hold. Some of the GC actions cause the Java application to pause (remember the UI freeze?). This will mostly happen when your application has a large heap (> 4GB). In those cases, GC tuning is required to shorten the pause time. After dealing with these issues in several Jenkins environments, my tip contains a few steps:

- Enable G1GC – this is the most modern GC implementation (default on JDK9)

- Enable GC logging – this will help you monitor and tune later

- Monitor GC behavior – I use http://gceasy.io/

- Tune GC with additional flags as needed

- Keep monitoring

