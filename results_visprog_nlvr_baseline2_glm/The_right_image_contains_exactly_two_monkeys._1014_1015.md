Question: The right image contains exactly two monkeys.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/a1/32/8f/a1328fcf176f12610f6535782665921f.jpg

Right image URL: http://4.bp.blogspot.com/-rnqJSkxWOPw/UilmJqJ2ZsI/AAAAAAAAAJU/WUU3Yu9HMwM/s1600/images.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many monkeys are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many monkeys are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many monkeys are in the image?')=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="3 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

