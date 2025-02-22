Question: There are two white drawers in the image on the left.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/a6/08/65/a6086585ff1b65977b4963d8ba514715.jpg

Right image URL: https://i.pinimg.com/736x/09/a4/5b/09a45b12068a056ff4c89058a1b053cb--bedroom-wardrobe-wardrobe-closet.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many white drawers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many white drawers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many white drawers are in the image?')=<b><span style='color: green;'>6</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="6 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

