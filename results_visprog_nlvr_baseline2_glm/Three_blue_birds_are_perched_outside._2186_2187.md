Question: Three blue birds are perched outside.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/d8/a9/18/d8a9184d3b46499adb14b508e619a797.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/83/dc/02/83dc023f5fb8c702a2afc439310043a4.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Three blue birds are perched outside.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Three blue birds are perched outside.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

