Question: The left image contains two men making a roof out of palm tree leaves.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/J4vDNphqnYQ/maxresdefault.jpg

Right image URL: http://thatchinginfo.com/wp-content/uploads/2016/07/29b1.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many men are making a roof out of palm tree leaves?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many men are making a roof out of palm tree leaves?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many men are making a roof out of palm tree leaves?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

