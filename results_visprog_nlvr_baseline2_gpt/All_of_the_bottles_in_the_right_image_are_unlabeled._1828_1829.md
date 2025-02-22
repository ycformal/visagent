Question: All of the bottles in the right image are unlabeled.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/c3/c6/d1/c3c6d18bc9c62ee1dceab1533706b0b9--pop-bottles-still-life-art.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/36/be/40/36be40004d966750a8e32b4227ccc542.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles in the image unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles in the image unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are all of the bottles in the image unlabeled?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

