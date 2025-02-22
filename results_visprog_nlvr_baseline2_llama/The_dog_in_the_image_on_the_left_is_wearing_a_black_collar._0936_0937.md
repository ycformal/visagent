Question: The dog in the image on the left is wearing a black collar.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/00/11/0f/00110fc444bec868c52be5c21b9031e8.jpg

Right image URL: https://media4.s-nbcnews.com/j/msnbc/components/video/201705/x_tdy_ov_pets_bulldog_bath_170505.nbcnews-ux-1080-600.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the dog wearing a black collar?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the dog wearing a black collar?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog wearing a black collar?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

