Apache CloudStack API Wrapper
=============================

This project is a minimalist wrapper around the Apache CloudStack (ACS) API.  Its
purpose is to provide an ACS library that works independent of the ACS version.
Instead of having function stubs for all of the ACS features, this lib is used
in conjunction with the ACS API documentation and the `request` function takes
the JSON values needed for each call.

It is expected that you refer to the ACS documentation while using this lib:
https://cloudstack.apache.org/api.html

There are two ways in which this lib can be consumed:

1. The `API` class can be instantiated from any code.  It has a single `request`
 method, which is used to make API calls against ACS.  This method takes a python 
 dictionary of request parameters and returns a python dictionary with the result.

2. The `CLI` class is a subclass of `API` and is designed to be a convenience
 class for working with stand alone scripts that populate the `API` constructor
 using command line arguments parsed by `docopt`.  The command line arguments can be
 passed in directly or they can be added to a JSON file and the `--json` flag can
 be used to reference the JSON file path. A `cli_example.py` file is included in
 the package to give a working example of how to use this use case.

The core of this library is a single `request` method which is described as follows.

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

**An example using the parent `API` class:**

``` python
from csapi import API
api = API(api_key="your_api_key", 
          secret_key="your_secred_key", 
          endpoint="http://127.0.0.1:8080/client/api")
accounts = api.request({
    'command':'listAccounts'
})
```

**An example using the `CLI` sub-class:**

``` python
from csapi import CLI
api = CLI(__doc__)
accounts = api.request({
    'command':'listAccounts'
})
```


INSTALL
=======

The easiest way to install this library is through `pip`.

``` bash
$ pip install csapi
```

Alternatively, you can pull down the source code directly and install manually.

``` bash
$ git clone https://github.com/swill/csapi.git
$ cd csapi
$ python setup.py install
```


USAGE
=====

The core functionality is documented above, but it is worth spending a minute
to better describe the `CLI` use case.  

``` bash
$ ./cli_example.py --help

Usage:
  cli_example.py [--json=<arg>] [--api_key=<arg> --secret_key=<arg>] [options]
  cli_example.py (-h | --help)

Options:
  -h --help                 Show this screen.
  --json=<arg>              Path to a JSON config file with the same names 
                              as the options (without the -- in front).
  --api_key=<arg>           CS Api Key.
  --secret_key=<arg>        CS Secret Key.
  --endpoint=<arg>          CS Endpoint 
                              [default: http://127.0.0.1:8080/client/api].
  --poll_interval=<arg>     Interval, in seconds, to check for a result on async jobs 
                              [default: 5].
  --logging=<arg>           Boolean to turn on or off logging [default: True].
  --log=<arg>               The log file to be used [default: logs/cs_api.log].
  --clear_log=<arg>         Removes the log each time the API object is created 
                              [default: True].
  --async=<arg>             Boolean to specify if the API should wait for async calls 
                              [default: False].
```

