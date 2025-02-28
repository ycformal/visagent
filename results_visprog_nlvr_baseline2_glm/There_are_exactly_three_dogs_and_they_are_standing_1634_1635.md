Question: There are exactly three dogs and they are standing

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/56/32/6c/56326c57e1798f1ad0139480a8013aa0.jpg

Right image URL: https://i.ytimg.com/vi/cZuNEWbUbuE/maxresdefault.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly three dogs and they are standing' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly three dogs and they are standing' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

