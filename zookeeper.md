
**What is ZooKeeper?**

ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them, which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.

**ZooKeeper Overview**

ZooKeeper allows distributed processes to coordinate with each other through a shared hierarchical name space of data registers (we call these registers znodes), much like a file system. Unlike normal file systems ZooKeeper provides its clients with high throughput, low latency, highly available, strictly ordered access to the znodes. The performance aspects of ZooKeeper allow it to be used in large distributed systems. The reliability aspects prevent it from becoming the single point of failure in big systems. Its strict ordering allows sophisticated synchronization primitives to be implemented at the client.

The name space provided by ZooKeeper is much like that of a standard file system. A name is a sequence of path elements separated by a slash ("/"). Every znode in ZooKeeper's name space is identified by a path. And every znode has a parent whose path is a prefix of the znode with one less element; the exception to this rule is root ("/") which has no parent. Also, exactly like standard file systems, a znode cannot be deleted if it has any children.

The main differences between ZooKeeper and standard file systems are that every znode can have data associated with it (every file can also be a directory and vice-versa) and znodes are limited to the amount of data that they can have. ZooKeeper was designed to store coordination data: status information, configuration, location information, etc. This kind of meta-information is usually measured in kilobytes, if not bytes. ZooKeeper has a built-in sanity check of 1M, to prevent it from being used as a large data store, but in general it is used to store much smaller pieces of data.



The service itself is replicated over a set of machines that comprise the service. These machines maintain an in-memory image of the data tree along with a transaction logs and snapshots in a persistent store. Because the data is kept in-memory, ZooKeeper is able to get very high throughput and low latency numbers. The downside to an in-memory database is that the size of the database that ZooKeeper can manage is limited by memory. This limitation is further reason to keep the amount of data stored in znodes small.

The servers that make up the ZooKeeper service must all know about each other. As long as a majority of the servers are available, the ZooKeeper service will be available. Clients must also know the list of servers. The clients create a handle to the ZooKeeper service using this list of servers.

Clients only connect to a single ZooKeeper server. The client maintains a TCP connection through which it sends requests, gets responses, gets watch events, and sends heartbeats. If the TCP connection to the server breaks, the client will connect to a different server. When a client first connects to the ZooKeeper service, the first ZooKeeper server will setup a session for the client. If the client needs to connect to another server, this session will get reestablished with the new server.

Read requests sent by a ZooKeeper client are processed locally at the ZooKeeper server to which the client is connected. If the read request registers a watch on a znode, that watch is also tracked locally at the ZooKeeper server. Write requests are forwarded to other ZooKeeper servers and go through consensus before a response is generated. Sync requests are also forwarded to another server, but do not actually go through consensus. Thus, the throughput of read requests scales with the number of servers and the throughput of write requests decreases with the number of servers.

Order is very important to ZooKeeper; almost bordering on obsessive–compulsive disorder. All updates are totally ordered. ZooKeeper actually stamps each update with a number that reflects this order. We call this number the zxid (ZooKeeper Transaction Id). Each update will have a unique zxid. Reads (and watches) are ordered with respect to updates. Read responses will be stamped with the last zxid processed by the server that services the read.

# What is Zookeeper Leader Election?
A server that has been chosen by an ensemble of servers, is what we call a Leader. Also, that leader continues to have support from that ensemble. Basically, to order client requests that change the ZooKeeper state is the main purpose of Leader.

Zookeeper State includes create, setData, and delete. Also, it transforms each request into a transaction. Furthermore, it proposes to the followers that the ensemble accepts and applies them in the order issued by the leader.

However, it enters the ELECTION state, when a process starts. And, the process tries to elect a new leader or become a leader, in this state. 

Hence, the process moves to the FOLLOWING state and begins to follow the leader when it finds an elected leader. So, we can say the processes in the FOLLOWING state are followers.

Moreover, the process moves to the LEADING state and becomes the leader, if the process is the leader after the election. 

# How is Leader elected in Zookeeper?
Before getting into the details of leader election, it's important to know what happens when a write occurs. Let's assume there are 3 servers, 1 one which is a leader and the remaining 2 followers. Every write goes through the leader and the leader generates a transaction id (zxid) and assigns it to this write request. The id represents the order in which the writes are applied to all replicas. A write is considered successful if the leader receives the ack from the majority (in this case 1 of the two followers need to ack). This is pretty much the flow for all the writes. The requirement of zxid is that it increases monotonically and is never re-used.

Now let's see what happens when the leader fails, each follower tries to become the leader by broadcasting the last zxid they have seen. Others reply OK if the zxid they have seen is less than or equal and NO if they have a higher zxid. You assume you are the leader if you get OK from the majority and broadcast the same to the followers.

This is a simplified version of the leader election. In a happy case, it looks simple and tempting to implement one. However, the challenge is to handle cases like network partitions, race conditions, ties, etc. Raft lecture talks about them in detail.

I would also suggest viewing the Raft lecture by John Ousterhout. Even though ZAB and Raft are seen as two different protocols, they are pretty much the same. The explanation of Raft is way better.

While creating znodes that represent “proposals” of clients, a simple way of doing leader election with ZooKeeper is to use the SEQUENCE|EPHEMERAL flags. Its basic concept is to have a znode, say “/election”, such that each znode creates a child znode “/election/n_” with both flags SEQUENCE|EPHEMERAL.

A sequence number which is higher than anyone previously appended to a child of “/election”, that is automatically appended by Zookeeper, with the sequence flag. In other words, Leader is a process which created the znode with the smallest appended sequence number.

Although make sure it is must watch for failures of the leader. Because if in the case the current leader fails, that helps a new client arises as the new leader.

There is one other solution for that. It is that to have all application processes keeping an eye upon the current smallest Znode, and also keep checking that when the smallest Znode goes away if they are the new leader.  Although this results in a herd effect.

That is all other processes receive a notification and execute getChildren on “/election” to obtain the current list of children of “/election”, upon of failure of the current leader. Also, it causes a spike in the number of operations that ZooKeeper servers have to process, if the number of clients is large. 

The pseudo code for ZooKeeper Leader Election is:

Let’s suppose ELECTION be a path of choice of the application. So, in order to volunteer to be a leader:

with path "ELECTION/n_", Create Znode z  with both SEQUENCE and EPHEMERAL flags;
Then let's suppose i be the sequence number of z and C be the children of "ELECTION";
Also, where j is the largest sequence number such that j < i and n_j is a Znode in C, watch for changes on "ELECTION/n_j";
Further, upon receiving a notification of Znode deletions:
Let’s suppose C be the new set of children of ELECTION;
Then execute leader procedure, if z is the smallest node in C;

Else, where j is the largest sequence number such that j < i and n_j is a Znode in C, watch for changes on “ELECTION/n_j”;

However, make sure that the Znode having no preceding znode on the list of children. Though it says it does not imply that the creator of this znode is aware that it is the current leader.

And, to acknowledge that the leader has executed the leader procedure, applications may consider creating a separate Znode.

# 1. Leader Election Basics
### 1.1 Definition
Sometimes horizontally scaling a system is as simple as spinning up a cluster of nodes and letting each node respond to whatever subset of the incoming requests they receive. At other times, the task at hand requires more precise coordination between the nodes and it’s helpful to have a leader node directing what the follower nodes work on.

A leader election algorithm describes how a cluster of nodes without a leader can communicate with each other to choose exactly one of themselves to become the leader. The algorithm is executed whenever the cluster starts or when the leader node goes down. 

### 1.2 When to use
There are three cases to consider when deciding if leader election fits the situation.

The first case is when each node is roughly the same and there isn't a clear candidate for a permanently assigned leader. This means any node can be elected as leader, and there isn’t a single point of failure required to coordinate the system.

The second case is when the cluster is doing particularly complex work that needs good coordination. Coordination can mean anything from decisions about how the work is to be divided, to assigning work to specific nodes, or to synthesizing the results of work from different nodes.

Let’s consider for example a scientific computation that is trying to determine how a protein folds. Because there are so many possible solutions, this computation can take a long time and will be sped up considerably if it’s distributed. The cluster will need a leader node to assign each node to work on a different part of the computation, and then add the results together to get the complete folded protein configuration.

The third case where leader election adds value is when a system executes many distributed writes to data and requires strong consistency. You can read more about consistency in our article on Databases, but essentially this means it's very important that no matter what node handles a request the user will always have the most up-to-date version of the data. In this situation a leader creates consistency guarantees by being the source of truth on what the most recent state of the system is (and the leader election algorithm must preserve this properly).

Not all applications require strong consistency, but you can imagine how it might be important to a bank to ensure that no matter what server answers a user's online banking request their bank account total will be accurate, and that multiple transactions directed to the same bank account won't conflict with each other.

### 1.3 Drawbacks
The main downside to leader election is complexity: a bad implementation can end up with “split brain” where two leaders try to control at the same time, or no leader is elected and the cluster can’t coordinate. As such, leader election should only be used when there is a need for complex coordination or strong consistency, and none of the alternatives fit the situation.

A leader is a single node, so it can become a bottleneck or temporary single point of failure. Additionally, if the leader starts making bad decisions (whatever that means in the context of directing work for the service), the followers will just do what they're assigned, possibly derailing the entire cluster.

The leader / follower model generally makes the best practices of partial deployment and A/B testing harder by requiring the whole cluster to follow the same protocols or be able to respond uniformly to the same leader.

Now that we've gone over the benefits and downsides of leader election, and you know when it's appropriate to use, let's jump into the algorithm approaches for implementing it!

## 2. Leader Election Algorithms
A leader election algorithm guides a cluster to collectively agree on one node to act as leader with as few back and forth communications as possible.

Generally, the algorithm works by assigning one of three states to each node: Leader, Follower, or Candidate. Additionally the leader will be required to regularly pass a "healthcheck" or “heartbeat” so follower nodes can tell if the leader has become unavailable or failed and a new one needs to be elected.

The kind of leader election algorithm you want depends on whether the cluster is synchronous or asynchronous. In a synchronous cluster nodes are synchronized to the same clock and send messages in predictable amounts of time and ordering. In an asynchronous cluster messages are not reliably delivered within a certain amount of time or in any order. 

In an asynchronous cluster any number of nodes can lag indefinitely so the leader election process can't guarantee both safety - that no more than one leader will be elected - and liveness - that every node will finish the election. In practice, implementations choose to guarantee safety because it has more critical implications for the service. 

Synchronous algorithms can guarantee both safety and liveness, and are therefore easier to reason about and theoretically preferable. But in practice the big drawback is synchronizing a cluster requires implementing additional constraints on how the cluster operates that aren’t always feasible or scalable.

Now let’s take a deeper look at the four most popular leader election algorithms.

#### 2.1 Bully Algorithm
The Bully Algorithm is a simple synchronous leader election algorithm. This algorithm requires that each nodes has a unique numeric id, and that nodes know the ids of all other nodes in the cluster.

The election process starts when a node starts up or when the current leader fails the healthcheck. There are two cases:

if the node has the highest id, it declares itself the winner and sends this message to the rest of the nodes.
if the node has a lower id, it messages all nodes with higher ids and if it doesn't get a response, it assumes all of them have failed or are unavailable, and declares itself the winner.
The main downside of the bully algorithm is that if the highest-ranked node goes down frequently, it will re-claim leadership every time it comes back online, causing unnecessary reelections. Synchronization of messages can also be difficult to maintain, especially as the cluster gets larger and physically distributed. 

### 2.2 Paxos
Paxos is a general consensus protocol that can be used for asynchronous leader election. Quite a lot of research has been done about the Paxos family of algorithms, which means it's both robust and there's much more to say about it than we have space for in this article.

Very briefly, Paxos uses state machine replication to model the distributed system, and then chooses a leader by having some nodes propose a leader, and some nodes accept proposals. When a quorum of (enough of) the accepting nodes choose the same proposed leader, that proposed leader becomes the actual leader.

### 2.3 RAFT
Raft is an alternative to Paxos that is favored because people tend to find it simpler to understand, and therefore easier to implement and use. Raft is an asynchronous algorithm.

In Raft consensus, each node keeps track of the current "election term". When leader election starts each node increments its copy of the term number and listens for messages from other nodes. After a random interval, if the node doesn't hear anything, it will become a candidate leader and ask other nodes for votes.

If the candidate ever reaches a majority of votes, it becomes a leader, and if it ever receives a message from another candidate with a higher term number, it concedes. The algorithm restarts if the election is split or times out without consensus. Restarts don't happen too often because the random timeouts help make it so nodes don't usually conflict.

### 2.4 Apache ZooKeeper (ZAB)
Apache Zookeeper is a centralized coordination service that is “itself distributed and highly reliable.” The ethos behind Apache ZooKeeper is that coordination in distributed systems is difficult, and it’s better to have a shared open source implementation with all the key elements so that your service doesn’t have to reimplement everything from scratch. This is especially helpful in large distributed systems.

ZAB (ZooKeeper Atomic Broadcast) is the protocol used by Apache ZooKeeper to handle leader election, replication order guarantees, and node recovery. It is called this because the leader “broadcasts” state changes to followers to make sure writes are consistent and propagated to all nodes. ZAB is an asynchronous algorithm.

ZAB is focused on making sure the history of the cluster is accurate through leadership transitions. The leader is chosen such that it has the most up to date history (it has seen the most recent transaction). When enough of the nodes agree that the new leader has the most up to date history, it syncs history with the cluster and finishes the election by recording itself as leader. 

## 3. Alternatives to leader election
Alternatives to leader election are based on the premise that coordination is possible without a dedicated leader node, thus achieving the primary function of leader election with lower implementation complexity.

Here’s a brief overview of three of the most notable alternatives:

### 3.1 Locking
A locking model ensures that concurrent operations on a shared resource don't conflict by only allowing changes from one node at a time. With optimistic locking a node will read a resource and its version id, make changes, and then before updating make sure that the version id is the same. If the id is different this means the resource has been updated since the node first read it. Going forward with the intended changes based on the old id would lose the other changes, so  the node needs to try again.

In pessimistic locking a node locks the resource, makes changes, and then unlocks the resource. If another node tries to initiate a change while the resource is locked, it will fail and try again later. Pessimistic locking is more rigorous, but can be hard to implement and bugs can cause deadlocks that stop a system from functioning.

These locking patterns are named for use cases. Optimistic locking is useful when you can make the "optimistic" assumption that another node won't change the resource out from under the operation. And pessimistic locking is useful when you can make the "pessimistic" assumption that there will be contention for the resource.

### 3.2 Idempotent APIs
APIs can have the feature of idempotency to ensure consistent interactions with a shared resource. An API is idempotent when the same request sent multiple times will not produce any inconsistent results. When reading from a resource, this means the response will always be the same value. When writing, this means the update will only happen once.

For example, idempotent writes can be implemented by requiring request ids so the system can tell if a request is being retried. Idempotency is also supported by other features we've talked about, like locking and database transactions.

An intuitive example of an idempotent API is bank account transfers: if a user initiates an online bank transfer and their internet goes down halfway through processing, you want to make sure the user can initiate the transfer again and your system will correctly only transfer the amount once.

### 3.3 Workflow Engines
Another way of coordinating nodes in a system is by using a workflow engine . A workflow engine is a centralized decision making system that contains a set of "workflows" of what work can be done, the state of data and work in the system, and the resources available to assign work to. Popular solutions are AWS Step Functions, Apache Airflow, and .NET State Machines.

## 4. Example leader election questions

Implement Leader Election with Kubernetes : https://kubernetes.io/blog/2016/01/simple-leader-election-with-kubernetes/
Design a Distributed Message Queue : https://serhatgiydiren.github.io/system-design-interview-distributed-message-queue
Implement Leader Election in Google Cloud : https://cloud.google.com/blog/topics/developers-practitioners/implementing-leader-election-google-cloud-storage



