Question: The right image shows a saxophone displayed with its bell facing the right and its mouthpiece at the upper left.

Reference Answer: True

Left image URL: https://cdn.shopify.com/s/files/1/0733/5373/products/sax_138_of_183_2048x2048.jpg?v=1477002015

Right image URL: https://www.dhresource.com/0x0s/f2-albu-g2-M00-92-E8-rBVaGlXpTy-AJKi3AAFC05xPuk8332.jpg/french-selmer-54-e-flat-alto-saxophone-top.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the saxophone displayed with its bell facing the right and its mouthpiece at the upper left?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the saxophone displayed with its bell facing the right and its mouthpiece at the upper left?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

