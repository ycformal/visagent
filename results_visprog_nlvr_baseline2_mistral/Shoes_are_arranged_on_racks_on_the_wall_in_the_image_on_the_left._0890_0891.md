Question: Shoes are arranged on racks on the wall in the image on the left.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/c3/52/2e/c3522e843aba439cc935c58346dd0401--new-balance--new-balance-shoes.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1qzYRLXXXXXcjXXXXq6xXFXXXX/Hot-sale-2016-new-running-shoes-for-men-free-flexible-cushion-sneakers-breathable-mesh-confortable-MD.jpg_640x640.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are shoes arranged on racks on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are shoes arranged on racks on the wall?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are shoes arranged on racks on the wall?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

