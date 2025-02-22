Question: The right image contains one dog chewing on a small object.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/67/67/3d/67673d545827f9acd87f506b5ac03558.jpg

Right image URL: http://www.famouschihuahua.com/wp-content/uploads/2011/08/jemma-chihuahua.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are chewing on a small object?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are chewing on a small object?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are chewing on a small object?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

