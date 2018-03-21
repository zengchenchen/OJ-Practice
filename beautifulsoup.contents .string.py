html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            <a class="external text" href="//tools.wmflabs.org/geohack/geohack.php?pagename=2018_Hualien_earthquake&amp;params=24.174_N_121.653_E_"><span class="geo-nondefault"><span class="geo-dms" title="Maps, aerial photos, and other data for this location"><span class="latitude">abc</span> <span class="longitude">def</span></span></span><span class="geo-multi-punct">﻿ / ﻿</span><span class="geo-default"><span class="geo-dec" title="Maps, aerial photos, and other data for this location">rfg</span><span style="display:none">﻿ / <span class="geo">24.174; 121.653</span></span></span></a>
        </p>
        <p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
c = soup.p.contents
print(c)
for t in c:
    print(t.string)
