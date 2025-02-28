Question: What color is his wetsuit?

Reference Answer: red and blue

Image path: ./sampled_GQA/319342.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is his wetsuit?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="What color is his wetsuit?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDOyKXIqqGpc17ypnnup5FnctJuFQZozVciIc2T7xSFxUWaM0+VC5mPL+1NL03NNJosgvIUtTCaCaaSKegrMQ4phxTiRTCRS5kPkY00UmRRS5kVyMkEx9KXzz6Cq++l8yrSRHMyyJz6Uvn+1Vd9L5lPlQc7LPnD0NJ53sar+ZSeZS5ULnZYM3saQy+xquZKQuaOVD52TmT603fmq5c00uaOVBzssFqaWqsXammQ+tTyl85Y3e9FVPMPrRS5Q5yDzLwdZF/Kl8y67yj/AL5r05PBXhtUQPq0pZuciMKMflSt4Q8MJz/a07Afwqgz/KuJYxFfVZ9zzDzLrqZePYUvmXOOZT/3z/8AXr0qXQ/CaQERrqUjr/FuVc/nxWHoWn6Pc6nfJqjTx2yEC32kBuvcjr+FL66L6rLuchvuD/y0pC1xjmU16RN4e8JAtt1e5UdsIpqt/YPhgD5ddnzg/wDLuOKf1sX1WXc89LTH/lq4/A01/NVHYzkBQTyTXoi+H/DZQsdcnU5xgwDP86wp7bRTHMIpNR88AgeZDGUIHTkNUyxcuhcMLrqzlYRNLCjM7hioJBzxTjazH/lo2frXUafpelLHg30qoAPLjS3yR+JIH61ds9L0ed9s15dx5OA/lJj8txNNYlpasJYa7utDiDaSn+NvzppspD/Ex/GvTz4U8P7N6684z0BhHH1ps3hTw6uduvSDIyMxggfWl9aBYVnmBsX9W/OivRpPDXh3cP8Aidy9O0f/ANeil9aY/qvmZMujzRsA2q2jMemJG/wqAWNyHx9vjUnuHb+gpRJMR1wPqaMyZ+8K47S7nXodjpLabZ2EcU9rY3FyoIZ2kbDe5+WhLjw2GIOlQb+p/wBIfb+GRXImWbHMv60oeT/npQoy7juux2m7ww+7FgigDOVmbPPbgVTlufDMYcf2a7Nn5SJZD/MVy5eXGPNYfTikJf8A56OaLT7iuuxvJqWgSIV/shgF6ZkfJ/Sq0k2jyrIfsLjbkgGVzk/lWSA2OHamnP8Aeb86XJLuO6JzLpykYsp/cCYgfqKtC/0NV50e6J/6+yP6VmbfUmm7QPX86ahLuF12Nb+09DDMRoUmewa5JFVHvrBnymmJGP8Arq5/+tVMhelN2j0quR9xXLcl9Cz5W3UD8f60VS2A96KXs33HdE/50p4BoopoQvQUAnH40UUwA9zSnrRRUgJ2pjMQ3XtRRSnsNDC7Y60uTRRSi2DEJ+akooq4iY0nmiiiqA//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is his wetsuit?')=<b><span style='color: green;'>red</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>red</span></b></div><hr>

Answer: red

