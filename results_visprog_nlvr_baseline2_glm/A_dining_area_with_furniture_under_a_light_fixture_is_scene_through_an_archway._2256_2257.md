Question: A dining area with furniture under a light fixture is scene through an archway.

Reference Answer: False

Left image URL: http://www.remodelista.com/wp-content/uploads/2015/03/fields/Ann-Stephenson-Fire-Island-A-frame-Kate-Sears-photo-Remodelista-2.jpg

Right image URL: https://i.pinimg.com/736x/ab/1f/ba/ab1fba4be234e9fd1fab95d9393d1771--built-in-corner-cabinet-built-in-china-cabinet.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A dining area with furniture under a light fixture is scene through an archway.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A dining area with furniture under a light fixture is scene through an archway.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

