#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  programa para saber la IP publica con la Raspberry en python3
  
import urllib.request
def public_ip():
        lista = "0123456789."
        ip=""
        dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
        for x in str(dato):
                if x in lista:
                        ip += x
        return ip
        


print(public_ip())
