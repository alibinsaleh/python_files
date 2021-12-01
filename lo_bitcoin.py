#!/usr/bin/env python3
'''
Title - Hello Bitcoin
This program demonstrates the creation of
- private key,
- public key
- and a bitcoin address.
'''

# import bitcoin
from bitcoin import *

my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)


