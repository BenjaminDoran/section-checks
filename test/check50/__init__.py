from cs50 import *

class Test(Checks):

    @check()
    def exists():
        """ hello.c exists."""
        self.require('hello.c')