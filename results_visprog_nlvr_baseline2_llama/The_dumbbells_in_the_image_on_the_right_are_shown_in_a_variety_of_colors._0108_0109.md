Question: The dumbbells in the image on the right are shown in a variety of colors.

Reference Answer: True

Left image URL: https://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/tVwAAOSwSypY92Wj/$_86.JPG

Right image URL: http://1.bp.blogspot.com/-AMTRpoKmVNs/VU0sEQmgPOI/AAAAAAAAHdw/mJ-9BmuS2tk/s1600/IMG_0068.JPG

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are the dumbbells in the image shown in a variety of colors?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are the dumbbells in the image shown in a variety of colors?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the dumbbells in the image shown in a variety of colors?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

