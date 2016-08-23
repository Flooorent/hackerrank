#!/usr/bin/python

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

MAX_SIZE = 100

def has_cycle(head):
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
        if length > MAX_SIZE:
            return True
    return False

