#!/usr/bin/env python2
import sys
import json

def add(funName, mapping, functions, parent=None, lst=[]):
	res = { "name" : funName, "parent" : parent }
	if funName in mapping:
                toAdd = list()
                for child in mapping[funName]:
                        if child in functions and not child in lst:
                                lst.append(child)
                                toAdd.append(add(child, mapping, functions, funName, lst))
                                lst.pop()
                if len(toAdd) > 0:
                        res["children"] = toAdd
	return res

def generate(fileName, start):
	calls = dict()
        functions = set()
	with open(fileName,'r') as f:
		for line in f:
			if line[0] == '\t':
				if prev in calls:
					calls[prev].add(line.strip())
				else:
					calls[prev] = set(line.strip())
			else:
				prev = line.strip()
                                functions.add(prev)
        return add(start, calls, functions)

if __name__ == "__main__":
	if len(sys.argv) == 2:
		startSymbol = "main"
	else:
		startSymbol = sys.argv[2]
	callGraph = generate(sys.argv[1], startSymbol)
	print json.dumps(callGraph)
