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
