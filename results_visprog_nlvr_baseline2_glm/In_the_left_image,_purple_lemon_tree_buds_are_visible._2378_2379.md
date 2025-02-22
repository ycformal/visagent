Question: In the left image, purple lemon tree buds are visible.

Reference Answer: True

Left image URL: https://foodandtools.files.wordpress.com/2012/03/dsc_0002_2.jpg

Right image URL: https://diy.sndimg.com/content/dam/images/diy/fullset/2016/5/3/0/Original_Felicia-Feaster-Orangerie-Liz-Locke.jpg.rend.hgtvcom.616.822.suffix/1462308126829.jpeg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are purple lemon tree buds visible?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are purple lemon tree buds visible?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are purple lemon tree buds visible?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

