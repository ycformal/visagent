Question: There are two dispensers in the image on the left.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1F2xbMXXXXXaDXXXXq6xXFXXX6/Simple-Wall-mounted-font-b-three-b-font-colors-hotel-toilet-bathroom-manual-350ML-ABS-Soap.jpg

Right image URL: https://i.pinimg.com/736x/cb/e8/ce/cbe8ce93389cf07d217c35a1b91bdb55--shampoo-dispenser-hotel-soap.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many dispensers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many dispensers are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many dispensers are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

