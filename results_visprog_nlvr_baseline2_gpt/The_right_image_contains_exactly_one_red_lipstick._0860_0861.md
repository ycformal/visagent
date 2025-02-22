Question: The right image contains exactly one red lipstick.

Reference Answer: True

Left image URL: http://www.izzysbeautyshoppe.com/image/PicBB2Df120s502x3.png

Right image URL: https://images-na.ssl-images-amazon.com/images/I/41v-Pfy-yWL.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many red lipsticks are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many red lipsticks are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many red lipsticks are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

