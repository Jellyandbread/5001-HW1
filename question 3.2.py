# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:34:55 2020

@author: Yijie
"""

import xml.dom.minidom
import re
dom=xml.dom.minidom.parse('D:/HKUST DDM/5001 Introduction to Computational and Modeling Tools/HW 1/blocklist.xml')
root = dom.documentElement


a = root.getElementsByTagName('emItem')
id=[]

for i in a:
    id.append(i.getAttribute('id'))
    
for i in id:
    condition=re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z_\-]{1,19}\.[com,cn,net,org]{1,3}$',i)
    if condition:
        i=id.index(i)
        print(a[i].toxml().split('\n')[0])