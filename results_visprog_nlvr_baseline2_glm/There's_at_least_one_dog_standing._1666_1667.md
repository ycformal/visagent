Question: There's at least one dog standing.

Reference Answer: True

Left image URL: http://img1.etsystatic.com/000/0/5242123/il_570xN.192092827.jpg

Right image URL: https://i.pinimg.com/736x/a1/b3/5b/a1b35b8a5dc963965108cb9e1cc6d889--sweet-peas-italian-greyhound.jpg

Original program:

```
Statement: There's at least one dog standing.
Program:
ANSWER0=VQA(image=LEFT,question='How many dogs are standing?')
ANSWER1=VQA(image=RIGHT,question='How many dogs are standing?')
ANSWER2=EVAL(expr='{ANSWER0} >= 1 or {ANSWER1} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There's at least one dog standing.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There's at least one dog standing.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

