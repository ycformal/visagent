Question: The picture on the left shows a malinois sitting down attached to a blue leash.

Reference Answer: True

Left image URL: https://i.pinimg.com/236x/da/6d/51/da6d511e304f60f262cab328329a157f--malinois-shepherd-malinois-dog.jpg

Right image URL: https://i.pinimg.com/736x/19/a3/dd/19a3dd2704f5503c99277d729f50a31c--exa-german-malinois.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a malinois sitting down attached to a blue leash?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a malinois sitting down attached to a blue leash?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show a malinois sitting down attached to a blue leash?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

