#!/usr/bin/python

class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

def reverse_print(head):
    data = []
    temp = head
    while temp:
        data.append(temp.data)
        temp = temp.next
    for i in range(len(data)):
        print(data[len(data)-i-1])

