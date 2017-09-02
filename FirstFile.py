

import os
from pprint import pprint

class testclass:
    message = ""

    def testdef(self):
        pprint("I did it")

    def printHelp(self, msg):
        print(msg)

a = testclass()
a.testdef()
a.printHelp("get to the chopper")

print("test")
pprint("test")

