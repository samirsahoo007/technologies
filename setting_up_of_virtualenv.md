## Python2.7 Virtualenv Setup

##### Installation
```
$ pip install virtualenv
```

##### Creation of virtualenv:
```
$ virtualenv -p python2.7 <desired-path>
```

#### Activate the virtualenv:
```
$ source <desired-path>/bin/activate
```

### Deactivate the virtualenv:
```bash
$ deactivate
```

Additional Steps:

If there is any certificate of specific company needs to be installed then

```pip install abc-certificate -i https://pypi.abc.com/simple```

For installing some module from other than default(https://pypi.python.org/simple) location use -i option

```pip install mymodule -i https://pypi.abc.com/simple```

OR

```pip install -r requirements.txt -i http://dist.repoze.org/zope2/2.10/simple/```

* Where "abc" could be the organisation name

$ cat requirements.txt 
```
--index https://pypi.abc.com/simple
ordereddict==1.1 
argparse==1.2.1 
python-dateutil==2.2 
matplotlib==1.3.1 
nose==1.3.0 
numpy==1.8.0 
pymongo==3.3.0 
psutil>=2.0
```

# Note:
If we remove the --index line, the packages will be downloaded from the default index url

[About Virtualenv](https://virtualenv.pypa.io/en/stable/)

###### To setup a new virtual enviornment with all the modules installed in one of the existing virtual environment #####

```
i. Activate the existing virtual environment
ii. fire this "pip freeze..." command
$ pip freeze > /tmp/requirements.txt
iii. deactivate
iv. Activate the new virtual environment
ii. fire this "pip install ..." command
$ pip install -r /tmp/requirements.txt
```


```
$ pip install psycopg2==2.4.1                     # Install specific version

$ pip install psycopg2==2.4.1 --no-cache-dir      # To avoid installing it from cache
```


