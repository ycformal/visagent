Question: The left image contains a white dog eating food.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/cL981BmPWjA/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/c8/19/01/c81901d017a3bfdfa1ce9a0ee0d14dea--samoyed-puppies-puppys.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a white dog eating food?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a white dog eating food?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a white dog eating food?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

