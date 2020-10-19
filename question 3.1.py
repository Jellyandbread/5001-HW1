# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 18:55:40 2020

@author: Yijie
"""

import xml.dom.minidom
import re
dom=xml.dom.minidom.parse('D:/HKUST DDM/5001 Introduction to Computational and Modeling Tools/HW 1/blocklist.xml')
root = dom.documentElement


a = root.getElementsByTagName('emItem')
blockid=[]

for i in a:
    blockid.append(i.getAttribute('blockID'))
    
for i in blockid:
    condition=re.match('^i.*\d$|^g.*\d$',i)
    if condition:
        i=blockid.index(i)
        print(a[i].toxml().split('\n')[0])