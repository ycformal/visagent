Question: In at least one image there are four standing zebras.

Reference Answer: False

Left image URL: https://st.focusedcollection.com/12176994/i/400/focused_148000015-stock-photo-herd-of-zebras-in-savannah.jpg

Right image URL: http://nickbrisbane.zenfolio.com/img/s/v-3/p1362787567-5.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>zebras</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>zebras</span></b></div><hr>

Answer: zebras

