import re
from check50 import *


class International(Checks):

    @check()
    def exists(self):
        """international exists."""
        self.require("international")

    @check("exists")
    def US_currency(self):
        """ on input 25 10 5 1 (.41) -> 4 """
        expected = "you can make change with 4 coins\n"
        actual = self.spawn("python international 25 10 5 1").stdout()
        if not re.match(expected, actual):
            err = Error(actual))
            raise err

    @check("exists")
    def other(self):
        """ on input 18 5 7 1 (1.41) -> 10 """
        expected = "you can make change with 10 coins\n"
        actual = self.spawn("python international 18 5 7 1").stdout()
        if not re.match(expected, actual):
            err = Error(actual))
            raise err
