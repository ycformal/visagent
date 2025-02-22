Question: In the left image there are two golf balls on top of boxes.

Reference Answer: False

Left image URL: https://http2.mlstatic.com/kaddygolf-pelotas-golf-titleist-prov1-nuevas-caja-x-12-D_NQ_NP_728227-MLA25674874513_062017-F.jpg

Right image URL: https://http2.mlstatic.com/pelotas-golf-titleist-pro-v1-con-tu-logo-o-nombre-D_NQ_NP_963546-MLA25631155838_052017-F.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many golf balls are on top of boxes?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many golf balls are on top of boxes?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many golf balls are on top of boxes?')=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="0 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

