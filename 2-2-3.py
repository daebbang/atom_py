import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOwrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdout=io.TextIOwrapper(sys.stderr.detach(),encoding="utf-8")

html = """
<html><body>
    <h1>find vs select</h1>
    <p>CSS 선택자를 사용 및 다중반환</p>
    <p>태그 선택자 사용 및 단일변환</p>
    </body></html>
    """
soup=BeautifulSoup(html, 'html.parser')
print('soup',soup)
