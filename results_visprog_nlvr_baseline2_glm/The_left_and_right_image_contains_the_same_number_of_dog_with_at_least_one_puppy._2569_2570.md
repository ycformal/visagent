Question: The left and right image contains the same number of dog with at least one puppy.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/55/f3/a8/55f3a80924b91c4352ed3efea93b01b8.jpg

Right image URL: http://www.findfast.org/dogs/vizsla.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

