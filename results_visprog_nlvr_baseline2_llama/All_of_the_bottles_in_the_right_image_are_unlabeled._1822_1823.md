Question: All of the bottles in the right image are unlabeled.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/--7Etug3DoOg/VmiZfBGX_cI/AAAAAAAAEwg/jvHfH-9TlKw/s1600/Olive_Oil_Some_Kind_Jam_ebay.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/00/00/9c/00009cdd34713a4001c4db208552e9f2--observational-drawing-painted-bottles.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are all of the bottles unlabeled?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

