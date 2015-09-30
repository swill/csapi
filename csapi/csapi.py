#!/usr/bin/env python

# Author: Will Stevens (CloudOps) - wstevens@cloudops.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import hmac
import hashlib
import json
import os
import pprint
import requests
import sys
import time
import urllib

class API(object):
    """
    Instantiate this class with the requred arguments, then use the 'request'
    method to make calls to the CloudStack API.

    api = API(**args)
    accounts = api.request({
        'command':'listAccounts'
    })
    """
    
    def __init__(
        self, 
        api_key,
        secret_key,
        endpoint="http://127.0.0.1:8080/client/api",
        poll_interval=5,
        logging=False,
        log="",
        clear_log=False):

        self.api_key = api_key 
        self.secret_key = secret_key
        self.endpoint = endpoint
        self.poll_interval = poll_interval
        self.logging = logging
        self.log = log
        self.log_dir = os.path.dirname(self.log)
        self.clear_log = clear_log
        
        if self.log_dir and not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        if self.clear_log and os.path.exists(self.log):
            open(self.log, 'w').close()


    def sign(self, params):
        def cs_quote(v):
            return urllib.quote(str(v).encode('utf-8'), safe=".-*_")

        # build the query string
        query = "&".join(sorted([
            "=".join((k, cs_quote(v))).lower()
            for k, v in params.items()
        ]))
        return base64.b64encode(
            hmac.new(
                self.secret_key.encode('utf-8'), 
                query.encode('utf-8'), 
                hashlib.sha1).digest()
            ).decode('utf-8').strip()
        
    def request(self, params, method=None):
        """
        Builds the request and returns a python dictionary of the result or None.

        :param params: the query parameters to be sent to the server
        :type params: dict

        :returns: the result of the request as a python dictionary
        :rtype: dict or None
        """
        if self.api_key and self.secret_key and 'command' in params:
            result = None
            params['response'] = 'json'
            params['apiKey'] = self.api_key
            params['signature'] = self.sign(params)

            if method and method.upper() == 'POST':
                response = requests.post(self.endpoint, data=params)
            else:
                response = requests.get(self.endpoint, params=params)

            if response.ok:
                result = response.json()
                result = result[(params['command']).lower()+'response']
            else:
                print response.text
               
            if self.logging:
                with open(self.log, 'a') as f:
                    if method:
                        f.write("%s %s" % (method.upper(), response.url))
                        f.write('\n')
                        pprint.pprint(params, f, 2)
                    else:
                        f.write("GET %s" % (response.url))
                        f.write('\n')
                    f.write('\n')
                    if response.ok:
                        #pprint.pprint(response.headers, f, 2)  # if you want to log the headers too...
                        pprint.pprint(result, f, 2)
                    else:
                        f.write(response.text)
                        f.write('\n')
                    f.write('\n\n\n')

            # if the request was an async call, then poll for the result...
            if result and 'jobid' in result.keys() and \
                    ('jobstatus' not in result.keys() or ('jobstatus' in result.keys() and result['jobstatus'] == 0)):
                print 'polling...'
                time.sleep(self.poll_interval)
                result = self.request({'command':'queryAsyncJobResult', 'jobId':result['jobid']})

            return result
        else:
            print("ERROR: --api_key, --secret_key and a request command param are all required to use the api...")
            return None


