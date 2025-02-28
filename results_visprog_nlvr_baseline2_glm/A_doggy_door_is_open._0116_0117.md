Question: A doggy door is open.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/z5LvvmnD_po/maxresdefault.jpg

Right image URL: https://www.dicksranchoglass.com/wp-content/uploads/2012/07/pet-door-after1.jpg

Original program:

```
Statement: A doggy door is open.
Program:
ANSWER0=VQA(image=LEFT,question='Is the doggy door open?')
ANSWER1=VQA(image=RIGHT,question='Is the doggy door open?')
ANSWER2=EVAL(expr='{ANSWER0} or {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A doggy door is open.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A doggy door is open.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

