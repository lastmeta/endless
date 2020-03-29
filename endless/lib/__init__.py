'''
1. start here
https://hub.docker.com/r/ipfs/go-ipfs#running-ipfs-inside-docker

2. use this
https://github.com/ipfs/py-ipfs-http-client

3. create API for managing identity

4. make demo
transfer source code over ipfs from one endless browser image to another
view results through mounted port via web UI
'''

# demo code
# make this a flask app
import os
from endless.api import identity
session = identity.login('some public key or something')
if session:
    print('logged in')
else:
    print('login failed')
