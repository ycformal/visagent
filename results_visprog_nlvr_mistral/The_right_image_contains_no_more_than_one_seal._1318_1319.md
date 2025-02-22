Question: The right image contains no more than one seal.

Reference Answer: False

Left image URL: http://wfsb.images.worldnow.com/images/8422268_G.jpg

Right image URL: https://cindyknoke.files.wordpress.com/2014/10/dsc00661.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='How many seals are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} <= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many seals are in the image?')=<b><span style='color: green;'>5</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 <= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="5 <= 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

