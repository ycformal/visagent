Question: In at least one image there is a mother gorilla behind her baby.

Reference Answer: False

Left image URL: http://cdn.cnn.com/cnnnext/dam/assets/160329141401-gorilla-fossey-fung-10-full-169.jpg

Right image URL: https://pbs.twimg.com/media/DKKsUw6W0AIe5r4.jpg

Original program:

```
The program is correct. It checks if there is a mother gorilla behind her baby in at least one image. If there is, the answer is True, otherwise False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

