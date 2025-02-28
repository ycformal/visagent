Question: The right image shows a row of standing bikini models with at least one model's rear turned to the camera.

Reference Answer: True

Left image URL: http://hollywoodpq.com/wp-content/uploads/2015/07/224-e1437162424167.jpg

Right image URL: http://y3.ifengimg.com/a/2014_46/51aaecf08cd52c3.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a row of standing bikini models with at least one model's rear turned to the camera.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a row of standing bikini models with at least one model's rear turned to the camera.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

