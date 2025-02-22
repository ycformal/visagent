Question: In the right image, people in purple attire are lined up in front of a temple.

Reference Answer: False

Left image URL: https://www.trekkinginsikkim.com/images/sikkim-monastery-tour4.jpg

Right image URL: https://i0.wp.com/www.placeforvacations.com/wp-content/uploads/2014/08/Phensang-Monastery-Famous-monastery-of-Sikkim.jpg?fit=810%2C608&ssl=1

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are people in purple attire lined up in front of a temple?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are people in purple attire lined up in front of a temple?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are people in purple attire lined up in front of a temple?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

