Question: All of the bottles in the right image are unlabeled.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-dpwjLOaI0WA/UcjlpU74iVI/AAAAAAAADHM/fW6ia34_H8o/s1600/Pepsi_and_Coke_post.jpg

Right image URL: https://i.pinimg.com/564x/3d/db/8a/3ddb8ae536e8c367d784cdf9e1d379fc--red-tops-realism-art.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are all of the bottles unlabeled?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are all of the bottles unlabeled?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

