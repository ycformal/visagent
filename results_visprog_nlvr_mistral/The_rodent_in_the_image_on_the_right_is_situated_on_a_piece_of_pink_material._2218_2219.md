Question: The rodent in the image on the right is situated on a piece of pink material.

Reference Answer: False

Left image URL: http://cf.ltkcdn.net/small-pets/images/std/193083-342x228-Teddy-Guinea-Pig.jpg

Right image URL: https://i.pinimg.com/736x/f3/cb/09/f3cb09b72daf457a5ebac7b994d049ff--pig-stuff-stuffed-animals.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the rodent situated on a piece of pink material?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the rodent situated on a piece of pink material?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

