Question: The right image contains at least one dog wearing a Santa Claus hat.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/64/15/4e/64154e2ccae741b7600dbcf7089e9c8c--bassett-hound-cat-boxes.jpg

Right image URL: https://i.pinimg.com/736x/67/eb/5e/67eb5e8c61b1d9096afd2dae2d788cdf--dog-boots-old-dogs.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are wearing a Santa Claus hat?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many dogs are wearing a Santa Claus hat?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dogs are wearing a Santa Claus hat?')=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="0 >= 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

