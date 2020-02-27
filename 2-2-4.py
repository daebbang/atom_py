import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOwrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdout=io.TextIOwrapper(sys.stderr.detach(),encoding="utf-8")

html="""
<html><body>
<div id="main">
 <h1>강의목록<h1>
<ul class="lecs">
    <li>java 초고수 되기</li>
    <li>파이선기초</li>
    <li>러닝머신</li>
    <li>안드로이드</li>
 </ul>
</div>
</html></body>
"""

prettify <html>
<body>
<div id="main">
<h1>
강의목록
</h1>
<ul class="lecs">
<li>
