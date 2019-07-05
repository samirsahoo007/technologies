# Examples

https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code/ec2
https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code/s3

## API

boto3

    # pip install boto3

## What are they?

	- An EC2(Elastic Computing Cloud) instance is like a remote computer running Windows or Linux and on which 
	you can install whatever software you want, including a Web server running PHP code and a database server.

	- Amazon S3(Simple Storage Service) is just a storage service, typically used to store large binary files.
	It's an object storage service that offers scalability, data availability, security, and performance.

## Can s3 be used with ec2 instances?

- S3 is object based storage and EBS and EFS are block based storage, you can mount only Block based storage device to an ec2 instance.
- S3 can not be mounted, however S3 objects can be accessed from any ec2 instance. you could mount s3 as a folder using s3fs, however, it would not act as a block device.

## Can you mount s3 to ec2?

- A S3 bucket can be mounted in a AWS instance as a file system known as S3fs. S3fs is a FUSE file-system that allows you to mount an Amazon S3 bucket as a local file-system.
- It behaves like a network attached drive, as it does not store anything on the Amazon EC2, but user can access the data on S3 from EC2 instance.

## Amazon EC2 vs. Amazon S3: What’s Similar, What’s Different?

- The former is a service for accessing cloud-based servers, while the latter is a storage service. They’re different types of things.

- That said, EC2 and S3 are closely related services. If you use one, there is a good chance you will use the other. That is particularly true for the following reasons:

- Amazon EC2 is a popular solution for hosting websites or Web apps in the Amazon cloud. For those use cases, Amazon S3 offers an easy and highly scalable means of hosting the static data that the website or Web app serves.
- S3 buckets can be used as a storage location for backing up data from inside EC2 instances. (As we explain in the article on how to back up Amazon EC2 instances, this is only one of several possible approaches for backing up EC2.)
 Because the same S3 storage bucket can be accessed by multiple EC2 instances, as well as various other types services on the AWS cloud, S3 is a useful solution for sharing data between EC2 instances and beyond. (Indeed, you could even 
 access S3 storage from applications that you host on-premise, so it’s a handy way of sharing data between the cloud and your local infrastructure.)

- On the other hand, EC2 and S3 don’t go hand-in-hand in all situations. Amazon S3 is not an ideal storage solution for hosting highly dynamic website data, like server-side session data. In addition, while there are several approaches available for backing up S3 data to local storage or to other locations in the cloud, backing up S3 buckets will back up only the data inside those buckets. Therefore, if you want to back up all of the data inside an EC2 instance -- including the data used to create the instance itself -- you need to use additional backup methods.

# Amazon EC2

It's just kind of a regular computer hosted somewhere on one of AWS data-center. And, as part of that it has a hard-drive or local storage. And, it is not permanent in the sense that anything that you want to store long term you don't want to store on the hard-drive of EC2 instance because of scaling-up and scaling-down while adding easy to servers, vice-versa(maintaining Elasticity property). And, so you don't want to have things that you want to keep forever on to the local storage because as you add or remove instances then you can potentially lost that information or lose that data. EC2 is meant to deploy your application on server(using its processing power) and that server serve the contents through the S3 and RDS, respectively. Hence, Amazon EC2 good for any type of processing activity.

# Amazon S3

Take an e.g. of Netflix that where they actually stores millions of physical video files that power their content. There have to be those video files and multiple versions of those store somewhere. That's where S3 comes into play. Amazon S3 is a storage platform of AWS. It's specially called large unlimited storage bucket(Limit is very high). So, S3 is perfect place for storing doc, movie, music, apps, pictures, anything you want to store, just dump onto S3. And, it's going to be multiple redundancies and back-up of files that you put there. So, again you are always going to have high availability of any files that you decide to store on S3.
Amazon S3 bucket is where Netflix stores the thousands of petabytes of video files.

# Examples of S3:

    Amazon S3 Buckets
    Uploading Files
    Downloading Files
    File Transfer Configuration
    Presigned URLs
    Bucket Policies
    Access Permissions
    Using an Amazon S3 Bucket as a Static Web Host
    Bucket CORS Configuration

# Examples of EC2:

    Managing Amazon EC2 Instances
    Working with Amazon EC2 Key Pairs
    Describe Amazon EC2 Regions and Availability Zones
    Working with Security Groups in Amazon EC2
    Using Elastic IP Addresses in Amazon EC2
