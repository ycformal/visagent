Question: The left image shows a blue lid propped on a blue box of 12 yellow golf balls with emoji faces.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1.nvtQXXXXXbwaXXXq6xXFXXXV/12-Pz-1-Scatola-di-Palline-Da-Golf-pallina-da-golf-Emoji-Facce-Divertenti-Novit-bel.jpg_640x640.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/41Rkxvo9WVL.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a blue lid propped on a blue box of 12 yellow golf balls with emoji faces?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a blue lid propped on a blue box of 12 yellow golf balls with emoji faces?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show a blue lid propped on a blue box of 12 yellow golf balls with emoji faces?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

