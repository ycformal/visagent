Question: The left image shows a staircase instead of a ladder leading up to a loft.

Reference Answer: False

Left image URL: https://notreadyforaarp.files.wordpress.com/2015/07/img_00131.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/71/fc/f3/71fcf32147d28540067da069301a3266--living-in-a-yurt-tent-living.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a staircase instead of a ladder leading up to a loft?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show a staircase instead of a ladder leading up to a loft?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

