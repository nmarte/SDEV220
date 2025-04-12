"""
To see all the places that your Python interpreter looks, 
import the standard sys module and use its path list. 
This is a list of directory names and ZIP archive files 
that Python searches in order to find modules to import.
"""

import sys
for place in sys.path:
    print(place)

# You can modify the search path within your code. 
# Let’s say you want Python to look in the /my/modules directory 
# before any other:

import sys
sys.path.insert(0, "/my/modules")
