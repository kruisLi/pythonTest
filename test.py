from enum import Enum
import re


class Coordinate(Enum):
    """
    Coordinate with binary codes that can be indexed by the int code.
    """

    def __init__(self, data):
        self.data = re.compile(data, re.I)


    HIGH_SCHOOL = r"high\sSCHOOL"


result = Coordinate['HIGH_SCHOOL'].data.search('high school')
print(result)
