import sys
import io
import urllib.request as dw

sys.stdout=io.TextIOwrapper(sys.stdout.detach(),encoding="utf-8")
sys.stdout=io.TextIOwrapper(sys.stderr.detach(),encoding="utf-8")

imgurl="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSb6OxtickwqxoJQrp23oUJs0Gb3iMUDurHtcbgCthfnVj3fJeP"

savePath1="D:/atom/atom"
savepath2="D:/atom"
dw.urlretaiave(imgurl, savePath1)
dw.urlretaiave(htmlURL, savepath2)


saveFile1=open(savepath1, 'wb')
saveFile1.wrtie(f)
saveFile1.close()

whih open(savepath2,'wb') as savepath2
    savepath2,write(f2)


print("다운로드 완료 ")
