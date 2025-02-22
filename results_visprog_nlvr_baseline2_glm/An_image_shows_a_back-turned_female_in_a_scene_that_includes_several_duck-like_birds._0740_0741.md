Question: An image shows a back-turned female in a scene that includes several duck-like birds.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/d6/f0/1f/d6f01fca14a0c118e3463169e5784d29.jpg

Right image URL: https://vvsphotography.files.wordpress.com/2012/05/02.jpg

Original program:

```
Statement: An image shows a back-turned female in a scene that includes several duck-like birds.
Program:
ANSWER0=VQA(image=LEFT,question='Is the female back-turned?')
ANSWER1=VQA(image=RIGHT,question='Is the female back-turned?')
ANSWER2=VQA(image=LEFT,question='Are there several duck-like birds in the scene?')
ANSWER3=VQA(image=RIGHT,question='Are there several duck-like birds in the scene?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

