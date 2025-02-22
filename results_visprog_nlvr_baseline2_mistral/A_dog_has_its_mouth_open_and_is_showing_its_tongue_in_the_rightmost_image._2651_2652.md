Question: A dog has its mouth open and is showing its tongue in the rightmost image.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/37/31/1e/37311ed3eb3eaa68060870bacf535511--miniature-schnauzer-spring.jpg

Right image URL: https://i.pinimg.com/736x/b5/bc/d3/b5bcd329d165a4cef23b4d657d64ec02--miniature-schnauzer-cute-dogs.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the dog have its mouth open and is showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the dog have its mouth open and is showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the dog have its mouth open and is showing its tongue?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

