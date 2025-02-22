Question: In the image to the right, several televisions are powered on.

Reference Answer: False

Left image URL: https://triadgoodwill.wordpress.com/files/2010/01/tv-003-e1262896351960.jpg?w=225

Right image URL: https://cdnph.upi.com/svc/sv/i/7661487353256/2017/1/14873535403832/Recycling-plant-worker-finds-100000-stashed-inside-30-year-old-TV.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many televisions are powered on?')
ANSWER1=EVAL(expr='{ANSWER0} > 0')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many televisions are powered on?')
ANSWER1=EVAL(expr='{ANSWER0} > 0')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many televisions are powered on?')=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 > 0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="0 > 0")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

