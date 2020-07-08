# -*- coding: utf-8 -*-

"""
@author: Franklin
@file: ipfs_test.py
@time: 2019/12/6 14:57
@dec: 
"""
 


import ipfshttpclient



api = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/9001/http')
print(api.cat("Qma39bHSpN5w1rYky9CtTXhwdgodrzZYfV2fmn8tASquyD"))
# api.cat("Qma39bHSpN5w1rYky9CtTXhwdgodrzZYfV2fmn8tASquyD")
res = api.add("TEST")
print(api.id)
print(api.swarm.peers)