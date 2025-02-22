Question: An entire bracelet is visible in the left image.

Reference Answer: True

Left image URL: http://img0.etsystatic.com/003/0/6211687/il_570xN.361829908_g5mf.jpg

Right image URL: https://img0.etsystatic.com/007/0/6474867/il_570xN.406854866_fff6.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Is an entire bracelet visible in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is an entire bracelet visible in the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

