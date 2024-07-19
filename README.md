# Web_scraping

### Weather_Scraping

Python 網路爬蟲練習
從中央氣象局的API 文件裡面抓取天氣報告

<img src="https://i.imgur.com/tI9wQcG.png" width="60%">  

在整個過程中我認為最麻煩的地方反而不是程式，而是在看文件的部分。要在一大堆的data 中找到真正需要的資訊花了我蠻多的時間。

另外，我在中央氣象局的網站上發現了儲存縣市和鄉鎮市區Id 的檔案，並把它改成json 檔，這樣未來在做地區的索引時會方便許多。只是這些檔案裡存的id 和API 文件裡的對應的`'geocode'` 有些不同。以台南市東區為例：它的id 是 `6703200` ，但在文件裡它的`'geocode'` 是 `67000320` 。這部分需要再做處理。

目前我寫的這個程式有一個限制，它只能抓取台南市的天氣報告，而其他縣市的不行。因此我打算修改一下，讓使用者可以自己輸入縣市和鄉鎮市區，並把這項功能整合到discord bot上。

## See also

[Discord bot](https://github.com/Guan-Yu-Chen/Discord_Bot)
