Question: In the image to the right, you can see the person's fingers.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/EyVXlVFA_-I/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/2a/b4/11/2ab411151cb378fa17b76d8b1bf9bccb.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the person')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

