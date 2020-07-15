
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

