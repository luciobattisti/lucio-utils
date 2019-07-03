"""
Little utility to convert tex formulas in md document to codecogs images.
"""

import re
import sys
from urllib.parse import quote


# General idea
# quote = "q(Z) = p(Z|X,\\theta)"
# quote = "https://latex.codecogs.com/gif.latex?" + urllib.parse.quote(quote)
# https://latex.codecogs.com/gif.latex?q%28Z%29%20%3D%20p%28Z%20%7C%20X%2C%20%09theta%29

# Open file
with open(sys.argv[1]) as fp:
    data = fp.read()

# Catch latex math formulas
tex_to_link = {}
for tex in re.findall("(\$.+?\$)", data):
    link = "https://latex.codecogs.com/gif.latex?" + quote(tex.replace("$", "").strip())
    tex_to_link[tex] = link

# Replace tex with link
for k,v in tex_to_link.items():
    print("Replace %s with %s" % (k,v))
    data = data.replace(k, "![equation](%s)" % v)

with open(sys.argv[2], "w") as fp:
    fp.write(data)



