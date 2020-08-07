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

```pip install -i https://pypi.abc.com/simple abc-certificate```

For installing some module from other than default(https://pypi.python.org/simple) location use -i option

```pip install -i https://pypi.abc.com/simple mymodule```

* Where "abc" could be the organisation name

[About Virtualenv](https://virtualenv.pypa.io/en/stable/)

###### To setup a new virtual enviornment with all the modules installed in one of the existing virtual environment #####

```
$ pip freeze > /tmp/requirements.txt	 # i. Activate the existing virtual environment and ii. fire this "pip freeze..." command and then iii. deactivate
$ pip install -r /tmp/requirements.txt   # i. Activate the new virtual environment and ii. fire this "pip install ..." command
```


```
$ pip install psycopg2==2.4.1                     # Install specific version

$ pip install psycopg2==2.4.1 --no-cache-dir      # To avoid installing it from cache
```


