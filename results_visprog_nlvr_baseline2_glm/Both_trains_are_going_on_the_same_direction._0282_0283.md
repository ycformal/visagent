Question: Both trains are going on the same direction.

Reference Answer: True

Left image URL: http://www.vicsig.net/interstate/nsw/20070222-sandgate-coal-5007-5009.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/8f/9e/86/8f9e8618ba01262db242b225d5cad35e.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Both trains are going on the same direction.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Both trains are going on the same direction.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

