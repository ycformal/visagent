Question: There are exactly six cups in the left image.

Reference Answer: False

Left image URL: https://officedepot.scene7.com/is/image/officedepot/508527_p_1_102617?$OD%2DLarge$&wid=450&hei=450

Right image URL: http://img1.tebyan.net/Big/1390/11/13813822242282461416714717910019183227103198.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many cups are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 6')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many cups are in the image?')=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 6")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="4 == 6")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

