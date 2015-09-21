# -*- coding: utf-8 -*-
def checkAttributes(t, d):
    for key in d.keys():
        if not getattr(t, key) == d[key]:
            assert False, "Timedelta Attribute: '{0}' not as expected {1}, received {2}".format(key, d[key], getattr(t, key))

def hasAttributes(t, d):
    for key in d:
        if not hasattr(t, key):
            assert False, "Timedelta Missing Attribute: '{0}' ".format(key)
