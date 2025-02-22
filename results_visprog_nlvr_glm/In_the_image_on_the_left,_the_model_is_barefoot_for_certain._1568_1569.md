Question: In the image on the left, the model is barefoot for certain.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/3d/43/1f/3d431ffa81ac8f5f2eb6395050bf1c62--bed-heads-mom-day.jpg

Right image URL: https://i.pinimg.com/736x/58/64/54/586454d1f7509c5249e56533da3c541f--coffee-in-bed-a-love.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Is the model barefoot?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)The statement is True.
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the model barefoot?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

