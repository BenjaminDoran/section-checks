import re
from check50 import *


class International(Checks):

    @check()
    def exists(self):
        """international exists."""
        self.require("international")

    @check("exists")
    def US_currency(self):
        """ on input .41 with denominations 25 10 5 1 yields 4 """
        expected = "4\n"
        actual = self.spawn("python international 25 10 5 1")\
                     .stdin('.41')\
                     .stdout("^4\n", expected)

    @check("exists")
    def other(self):
        """ on input 1.41 with denominations 18 5 7 1 yields 10 """
        expected = "10\n"
        actual = self.spawn("python international 18 5 7 1")\
                     .stdin('1.41')\
                     .stdout("^10\n", expected)
