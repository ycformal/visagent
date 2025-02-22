Question: At least one image shows a hitched dog sled team with several reclining dogs.

Reference Answer: False

Left image URL: http://alaskanmalamutes.us/images/wwI-nome-dogs-in-france.jpg

Right image URL: http://4.bp.blogspot.com/-L-5Aff4OKuA/U5TDddwfcmI/AAAAAAAAIqk/T_Ukd5_JbSw/s1600/Screen+Shot+2014-06-08+at+1.09.55+PM.png

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

