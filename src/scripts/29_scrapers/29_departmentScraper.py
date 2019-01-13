"""
scraping raw data for department
"""

import re

rawDataPath = "C:\\tools\\AutomatetheBoringStuff_Course\\src\scripts\\29_scrapers\\rawData\\"
#file = "singelData.txt"
file = "rawContactData.txt"

depIDRegex = re.compile("""
[a-z0-9@.!#$%&'*+/=?^_`{|}~-]*@[a-z0-9@.!#$%&'*+/=?^_`{|}~-]+[au|com|net]
""", re.VERBOSE | re.DOTALL)

# roleRegex = re.compile("""
# (\d{6,7}\s\w?-\d{5,6})
# """, re.VERBOSE)
#
# emailRegex = re.compile("""
# (\d{6,7}\s\w?-\d{5,6})
# """, re.VERBOSE)
#
# phoneRegex = re.compile("""
# (\d{6,7}\s\w?-\d{5,6})
# """, re.VERBOSE)

rawFileData = open(rawDataPath+file, mode="r")
fileData = rawFileData.read()

depID = depIDRegex.findall(fileData)

print(depID)
print(len(depID))

rawFileData.close()