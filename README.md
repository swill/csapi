Apache CloudStack API Wrapper
=============================
This project is a minimalist wrapper around the Apache CloudStack API.  Its purpose is to expedite the process of testing the API and building scripts to do useful tasks.

This project exposes a single `API` class which has a single `request` method.  This method takes a python dictionary of request parameters and returns a python dictionary with the result.

``` python
api.request(self, params)
```

``` sphinx
Builds the request and returns a python dictionary of the result or None.

:param params: the query parameters to be added to the url
:type params: dict

:returns: the result of the request as a python dictionary
:rtype: dict or None
```

Here is a simple example:

``` python
api = API(args)
accounts = api.request({
    'command':'listAccounts'
})
```


INSTALL
=======
This project does not need to be installed, it can be run in-place.  However, it does depend on a few libraries to keep things simple.

docops
------

``` bash
$ pip install docops
```

requests
--------

``` bash
$ pip install requests
```


USAGE
=====
The usage for this project is documented in the 'help' section of the scripts.

``` bash
$ ./cs_api.py --help
```

```
Usage:
  cs_api.py (--api_key=<arg> --secret_key=<arg>) [options]
  cs_api.py (-h | --help)

Options:
  -h --help                 Show this screen.
  --api_key=<arg>           CS Api Key.
  --secret_key=<arg>        CS Secret Key.
  --host=<arg>              CS IP or hostname (including port) 
                            [default: 127.0.0.1:8080].
  --protocol=<arg>          Protocol used to connect to CS (http | https) 
                            [default: http].
  --base_path=<arg>         Base CS Api path [default: /client/api].
  --poll_interval=<arg>     Interval, in seconds, to check for a result on 
                            async jobs [default: 5].
  --logging=<arg>           Boolean to turn on or off logging [default: True].
  --log=<arg>               The log file to be used [default: logs/cs_api.log].
  --clear_log=<arg>         Removes the log each time the API object is created 
                            [default: True].
```

``` bash
$ ./api_examples.py --help
```

```
Usage:
  api_examples.py (--api_key=<arg> --secret_key=<arg>) [options]
  api_examples.py (-h | --help)

Options:
  -h --help                 Show this screen.
  --api_key=<arg>           CS Api Key.
  --secret_key=<arg>        CS Secret Key.
  --host=<arg>              CS IP or hostname (including port) 
                            [default: 127.0.0.1:8080].
  --protocol=<arg>          Protocol used to connect to CS (http | https) 
                            [default: http].
  --base_path=<arg>         Base CS Api path [default: /client/api].
  --poll_interval=<arg>     Interval, in seconds, to check for a result on 
                            async jobs [default: 5].
  --logging=<arg>           Boolean to turn on or off logging [default: True].
  --log=<arg>               The log file to be used [default: logs/cs_api.log].
  --clear_log=<arg>         Removes the log each time the API object is created 
                            [default: True].
```

This project can be run as a stand alone script or the `API` object can be imported into other scripts in this directory as a library.

`cs_api.py` is a stand alone script which can be run on its own, as well as a basic library which can be imported into other scripts.

`api_examples.py` is an example of using the `cs_api.py` script as a library.  In this example, we  simply import the `API` object and start making requests.  This is ideal if you have multiple scripts that do different tasks and you want them to all exist at the same time.  Simply duplicate this file and change the api requests as needed.

