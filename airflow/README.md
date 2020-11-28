# Setup using docker

```
docker pull puckel/docker-airflow
docker build --rm --build-arg AIRFLOW_DEPS="datadog,dask" --build-arg PYTHON_DEPS="flask_oauthlib>=0.9" -t puckel/docker-airflow
docker run -d -p 8080:8080 puckel/docker-airflow webserver

OR

docker run -d -p 8080:8080 -e LOAD_EX=y puckel/docker-airflow	#  If you want to have DAGs example loaded (default=False)
```

If you want to run another executor, use the other docker-compose.yml files provided in this repository.

```
git clone https://github.com/puckel/docker-airflow.git
docker-compose -f docker-compose-LocalExecutor.yml up -d	# For LocalExecutor :

docker-compose -f docker-compose-CeleryExecutor.yml up -d	# For CeleryExecutor
```

If you want to use Ad hoc query, make sure you've configured connections: Go to Admin -> Connections and Edit "postgres_default" set this values (equivalent to values in airflow.cfg/docker-compose\*.yml) :

```
Airflow: localhost:8080
Flower: localhost:5555

Host : postgres
Schema : airflow
Login : airflow
Password : airflow
```

For encrypted connection passwords (in Local or Celery Executor), you must have the same fernet_key. By default docker-airflow generates the fernet_key at startup, you have to set an environment variable in the docker-compose (ie: docker-compose-LocalExecutor.yml) file to set the same key accross containers. To generate a fernet_key:

```
docker run puckel/docker-airflow python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)"
```

Scale the number of workers

```
docker-compose -f docker-compose-CeleryExecutor.yml scale worker=5
```

Running other airflow commands

```
docker run --rm -ti puckel/docker-airflow airflow list_dags

OR

docker-compose -f docker-compose-CeleryExecutor.yml run --rm webserver airflow list_dags

OR

docker run --rm -ti puckel/docker-airflow bash
docker run --rm -ti puckel/docker-airflow ipython
```

Ref: https://github.com/puckel/docker-airflow


Airflow is, it’s an workflow engine of the similar likes of Oozie and Azkaban. It’s based on the concept of a DAG which you write in Python and execute on a cluster.


Airflow — it’s not just a word Data Scientists use when they fart. It’s a powerful open source tool originally created by Airbnb to design, schedule, and monitor ETL jobs. But what exactly does that mean, and why is the community so excited about it?

Airflow is a WMS(workflow management systems) that defines tasks and and their dependencies as code, executes those tasks on a regular schedule, and distributes task execution across worker processes. Airflow offers an excellent UI that displays the states of currently active and past tasks, shows diagnostic information about task execution, and allows the user to manually manage the execution and state of tasks.

## Background: OLTP vs. OLAP, Analytics Needs, and Warehouses

Every company starts out with some group of tables and databases that are operation critical. These might be an orders table, a users table, and an items table if you’re an e-commerce company: your production application uses those tables as a backend for your day-to-day operations. This is what we call OLTP, or Online Transaction Processing. A new user signs up and a row gets added to the users table — mostly insert, update, or delete operations.
As companies mature (this point is getting earlier and earlier these days), they’ll want to start running analytics. How many users do we have? How have our order counts been growing over time? What are our most popular items? These are more complex questions and will tend to require aggregation (sum, average, maximum) as well as a few joins to other tables. We call this OLAP, or Online Analytical Processing.
The most important differences between OLTP and OLAP operations is what their priorities are:

* OLTP’s priority is maintaining data integrity and processing a large number of transactions in a short time span

* OLAP’s priority is query speed, and transactions tend to be batched and at regular intervals (ETL Jobs, which we’ll look at later)


![alt text](https://github.com/samirsahoo007/bigdata/blob/master/technologies/airflow/images/OLTPvsOLAP.png)

Accordingly, OLTP related queries tend to be simpler, require little aggregation and few joins, while OLAP queries tend be larger, more complex, and require more aggregations and joins.
In your e-commerce app, you might want to insert a new row into the orders table when a user makes a new order. These queries are pretty simple: they’ll probably boil down to something like INSERT INTO users VALUES x,y,z.
Answering those analytics-type OLAP questions is a different story though: they tend to involve much more data (aggregating order value over an entire table, for example) and require more joins to other database tables. If we wanted to see the total order value for users who live in New York, we’d need to use both an aggregation (sum of order value from the orders table) and a join (filter for New York addresses from the users table).
Early on in the company lifecycle, OLAP type queries and OLTP type queries will be run on your normal production database — because that’s all you have. But over time, OLAP usually starts to become too burdensome to run on your production tables:


* OLAP queries are more computationally expensive (aggregations, joins)

* OLAP often requires intermediate steps like data cleaning and featurization

* Analytics usually runs at regular time intervals, while OLTP is usually event based (e.g. a user does something, so we hit the database)

For these reasons and more, Bill Inmon, Barry Devlin, and Paul Murphy developed the concept of a Data Warehouse in the 1980’s. A warehouse is basically just another database, but it’s not used for production (OLTP) — it’s just for analytics (decision support, in their language). It’s designed and populated with all of the above analytics concerns instead of the OLTP requirements for running your app.


## Why did we chose Airflow?

To simplify (and slightly oversimplify):

> We didn’t have a consistent view of the results of the latest workflows.

> Logs required in debugging were located on several servers and in multiple applications.

> Basis for any kind of automation was minimal to non-existent.

> Error logging was very generic, with no easy way of knowing what was the root cause.

> Restarting a single task run was difficult, without visibility into the jobs logic.

> Dependencies between the tasks were hidden and the master workflows had created additional and unnecessary dependencies.

> To have a complete monitoring environment, we would have needed to build a separate environment for data collection and visualisation.


## ETL Jobs and Cron

Where things get interesting is how you actually get data into your warehouse. A typical modern warehouse setup will have many different types of data, like for example:

* Daily snapshots of production tables (to lessen the load on production)

* Product lifecycle events (consumed from some stream like Kafka)

* Dimension and fact tables (from the Star Schema)

These all come from different places, and require unique jobs to get the data from the source (extract), do whatever you need to get it ready for analytics (transform), and deposit it in the warehouse (load). This process is called ETL (Extract, Transform, Load), and each individual job we need is called an ETL job. So how exactly do we build those?

The classic approach (other than expensive vendors) has usually been Cron Jobs. Cron is a utility that runs in your terminal and lets you run programs at specific intervals (say, 2AM every other day). The code required for the ETL job is packaged into a file and scheduled on Cron. The problem, though, is that Cron wasn’t built for this type of work, and it shows. Some of the major issues that data teams face scheduling ETL jobs with Cron:

* ETL jobs fail all the time for a million reasons, and Cron makes it very difficult to debug for a number of reasons

* ETL tends to have a lot of dependencies (on past jobs, for example) and Cron isn’t built to account for that

* Data is getting larger, and modern distributed data stacks (HDFS, Hive, Presto) don’t always work well with Cron

Unsurprisingly, data teams have been trying to find more sophisticated ways to schedule and run ETL jobs. Airflow is one of the things we’ve come up with, and it’s pretty great.

## Core Concepts

Operators, Tasks, DAGs, XComs, , variables, reacap, cannextion, Hooks


# What we learned migrating off Cron to Airflow

The VideoAmp data engineering department was undergoing pivotal change last fall. The team at the time consisted of three data engineers and a system engineer who worked closely with us. We determined as a team how to prioritize our technical debt.

At the time, the data team was the sole owner of all the batch jobs that provided the feedback from our real-time bidding warehouse to the Postgres database that populated the UI. Should these jobs fail, the UI would be out of date and both our internal traders and external customers would be making decisions on stale data. As a result, meeting the SLAs of these jobs was critical to the success of the platform. Most of these jobs were built in Scala and utilized Spark. These batch jobs were orchestrated by Cron — a scheduling tool built into Linux.

### Pros of Cron

We identified that Cron was causing a few major pain points that were greater than its benefits. Cron is built into Linux, so it requires no installation out of the box. In addition, Cron is fairly reliable which makes it an appealing option. As a result, Cron is a great option for proof of concept projects. However, scaling with Cron doesn’t work well.
Image for post
Crontab file: How applications used to be scheduled

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/technologies/airflow/images/cron.png)

### Cons of Cron

The first problem with Cron was that changes to the crontab file were not easily traceable. The crontab file contains the schedule of jobs to run on that machine. This file contained the scheduling of jobs across projects yet it was never tracked in source control or integrated into the deployment process of a single project. Instead, engineers would edit as needed, leaving no record of edits across time or project dependencies.

The second problem was that job performance was not transparent. Cron keeps a log of job outputs on the server where the jobs were run — not in a centralized place. How would a developer know if the job is successful or failed? Parsing a log for these details is costly both for developers to navigate and expose to downstream engineering teams.

Lastly, rerunning jobs that failed was ad hoc and difficult. By default Cron has only a few environment variables set. A novice developer is often surprised to find the bash command stored in the crontab file will not result in the same output as their terminal, because their bash profile settings have been stripped from the Cron environment. This requires the developer to build up all dependencies of the environment of the user that executes the command.

Clearly, many tools need to be built on top of Cron for it to be successful. While we had a few of these issues marginally solved, we knew that there were many open source options available with more robust feature sets. Collectively, our team had worked with orchestration tools such as Luigi, Oozie, and other custom solutions, but ultimately our experience left us wanting more. The promotion of AirBnB’s Airflow into the Apache Incubator meant it held a lot of promise.

### Setup and Migration

In typical hacker fashion, we commandeered resources from the existing stack in secret to prove out our concept by setting up an Airflow metadb and host.

This metadb holds important information such as Directed Acyclic Graph (DAG) and task inventory, performance and success of jobs, and variables for signaling to other tasks. The Airflow metadb can be built on top of a relational database such as PostgreSQL or SQLite. By having this dependency, airflow can scale beyond a single instance. We appropriated a PostgreSQL RDS box that was used by another team for a development environment (their development sprint was over and they were no longer utilizing this instance).

The Airflow host was installed on our spark development box and was part of our spark cluster. This host was set-up with LocalExecutor and runs the scheduler and UI for airflow. By installing on an instance in our spark cluster, we gave our jobs access to the spark dependencies they needed to execute. This was key to successful migration that had prevented previous attempts.

Migration from Cron to Airflow came with its own challenges. Because Airflow was now owning the scheduling of tasks, we had to alter our apps to take inputs of a new format. Luckily, Airflow makes available the necessary meta information to the scheduling scripts via variables. We also stripped our applications of much of the tooling we had built into them, such as push alerting and signaling. Lastly, we ended up splitting up many of our applications into smaller tasks to follow the DAG paradigm.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/technologies/airflow/images/airflow.png)

Airflow UI: A developer can clearly discern from the UI which Dags are stable and which are not as robust and require hardening.


### Lessons learned

1. Applications were bloated By using Cron, scheduling logic had to be tightly coupled with the application. Each application had to do the entire work of a DAG. This additional logic masked the unit of work that was at the core of the application’s purpose. This made it both difficult to debug and to develop in parallel. Since migrating to Airflow, the idea of a task in a DAG has freed the team to develop robust scripts focused on that unit of work while minimizing our footprint.

2. Performance of batch jobs improved prioritization By adopting the Airflow UI, the data team’s batch job performance was transparent to both the team and to other engineering departments relying on our data.

3. Data Engineers with different skill sets can build a pipeline together Our data engineering team utilizes both Scala and Python for executing Spark jobs. Airflow provides a familiar layer for our team to contract between the Python and Scala applications — allowing us to support engineers of both skill sets.

4. The path to scaling scheduling of our batch jobs is clear With Cron, our scheduling was limited to the one machine. Scaling the application would require us to build out a coordination layer. Airflow offers us that scaling out of the box. With Airflow, the path is clear from LocalExecutor to CeleryExecutor, from CeleryExecutor on a single machine to several Airflow workers.

5. Rerunning jobs has become trivial With Cron, we would need to grab the Bash command that executed and hope that our user environment was similar enough to the Cron environment to recreate the error for us to debug. Today, with Airflow, it is straightforward for any data engineer to view the log, understand the error, and clear the failed task for a rerun.

6. Alerting levels are appropriate Prior to Airflow, all alerts for batch jobs would be sent to the same email alias as alerts for our streaming applications. With Airflow, the team built a Slack operator that can uniformly be called for all DAGS to push notifications. This allowed us to separate the urgent failing notifications from our real-time bidding stack from the important — but not as immediate — notifications from our batch jobs.

7. One poorly behaving DAG could bring down the whole machine Set guidelines for your data team to monitor the external dependencies of their jobs so as not to impact the SLAs of other jobs.

8. Rotate your Airflow logs This should go without saying, but Airflow is going to store the logs of the applications it calls. Be sure to rotate logs appropriately to prevent bringing down the whole machine from lack of disk space.

Five months later, the data engineering team at VideoAmp has nearly tripled in size. We manage 36 DAGs and counting! Airflow has scaled to allow all of our engineers to contribute and support our batch flows. The simplicity of the tool has made the on boarding of new engineers relatively pain-free. The team is quickly developing improvements like uniform push alerting to our slack channel, upgrading to Python3 Airflow, moving to CeleryExecutor, and making use of the robust features Airflow provides.


# Apache Airflow – why everyone working on data domain should be interested of it?

At some point in your profession, you must have seen a data platform where Windows Task Scheduler, crontab, ETL -tool or cloud service starts data transfer or transformation scripts independently, apart from other tools and according to the time on the wall. Your scripts presumably operate just fine most of the time, but adding new material or just understanding the whole extent of your data pipelines is sometimes surprisingly hard. Understanding dependencies and controlling data pipelines is also profoundly troublesome. You can only dream of Data Lineage when you can’t even have decent history data or success rate of your current data pipeline executions (unless you count email notifications as such). Keep reading if all of this sounds even remotely familiar as Apache Airflow might solve your obstacles as efficiently as ice hockey player Patrik Laine does in a man advantage below the left faceoff circle.

The issue pictured above is no way new and there actually have been numerous solutions at market meant to solve the matter. Outlining Enterprise -level solutions, there are few good competitors at open source market at this moment created to manage Hadoop -jobs; Oozie by Apache, Azkaban by LinkedIn and Luigi from Spotify. <b>Solutions which can handle other than pure Hadoop -jobs haven’t existed until now and Apache Airflow attempts to fill the gap.</b>

## What the is a DAG?

DAG is abbreviation from “Directed acyclic graph” and according to Wikipedia means “a finite directed graph with no directed cycles. That is, it consists of finitely many vertices and edges, with each edge directed from one vertex to another, such that there is no way to start at any vertex v and follow a consistently-directed sequence of edges that eventually loops back to v again.”.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/technologies/airflow/images/dag.png)

Simple DAG. Each of the boxes represent independent DAG task which could be anything from bash command to SQL or Hive -query.

Basically, DAG is a tree-like structure where you can define dependencies between various tasks and those tasks can branch out in a way where they will be executed regardless of the outcome of the other branch. To make things clear, this means that you can set dependencies between cron -jobs in an away where they could start or choose not start regardless of the outcome of other cron -jobs.

![alt text](https://github.com/samirsahoo007/bigdata/blob/master/technologies/airflow/images/dag2.png)

<b>Say goodbye to line drawing and say hello to automatically generated Python -code</b>

The fact that DAGs are based on Python-code is the neatest feature of Airflow. You can automate code generation, save it into version control and see what’s really happening in the data pipeline just by looking at the actual code itself. Metadatabase is just for saving the execution history so you don’t need to even worry about the performance concerns caused by multiple DAGs running simultaneously. Python -code also makes it possible you to write your own libraries or executors and add them without you requiring to wait for the fixed software release cycle set up by the current software vendors.

DAGs also solve many headaches which are currently fixed by creating separate verification jobs or by building several, separate tasks. What I mean by this is that you can have source staging load which triggers four separate tasks which eventually trigger even more tasks. In Airflow you can build a DAG where one failing task does not invalidate the whole data pipeline. Instead, only the tasks directly linked to that failing task are invalided. Building and maintaining something like this in cron would be a nightmare.


# Summary

When comparing with the list introduced at the beginning of this article, this is how the situation has changed:

> All data warehouse and analytics workflows are scheduled and managed in the one place, with easy access to a comprehensive view of the status.

> Execution logs are centralized to single location.

> With Airflow’s Configuration as a Code approach, we have been able to automate the generation of workflows to a very high degree.

> If a DAG fails, we receive a comprehensive error message in Slack immediately.

> Metadata enables us to regenerate individual uploads, if necessary.

> We have clear view the dependencies directly within the DAGs.

> Airflow contains out-of-the box charts that make it easy to examine run times and the ordering of the executions. Using Airflow’s own database and Grafana, for example, it’s easy to create more visualisations for more comprehensive monitoring.


Ref: https://medium.com/datareply/airflow-lesser-known-tips-tricks-and-best-practises-cf4d4a90f8f

