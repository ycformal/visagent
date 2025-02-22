Question: the right side has bananas as dolphins

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/4d/5f/b7/4d5fb7331dcd8cebcd3ad35e57c67b6b--banana-art-food-decorations.jpg

Right image URL: https://i.ytimg.com/vi/1qijns1uojo/maxresdefault.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas shaped like dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are there bananas shaped like dolphins?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there bananas shaped like dolphins?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

