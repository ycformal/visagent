Question: There is a single gorilla in the left image.

Reference Answer: False

Left image URL: http://cdn.cnn.com/cnnnext/dam/assets/160329141401-gorilla-fossey-fung-10-full-169.jpg

Right image URL: https://pbs.twimg.com/media/DKKsUw6W0AIe5r4.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many gorillas are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many gorillas are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many gorillas are in the image?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 == 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

