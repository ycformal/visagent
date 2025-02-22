Question: You can see the keyboard to the laptop on the right.

Reference Answer: True

Left image URL: http://molempire.com/app/uploads/2011/06/DesCom_Laptop_Concept.jpg

Right image URL: https://www.gizbot.com/img/2016/08/17-1471439717-gelfrog.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the keyboard to the laptop?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the keyboard to the laptop?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the keyboard to the laptop?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

