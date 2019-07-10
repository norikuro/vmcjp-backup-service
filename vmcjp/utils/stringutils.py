#!/usr/bin/env python

def replace_strings_in_list(ls, st):
#  return [l.replace(st, "") for l in ls]
  return [l.translate(None, st) for l in ls]
