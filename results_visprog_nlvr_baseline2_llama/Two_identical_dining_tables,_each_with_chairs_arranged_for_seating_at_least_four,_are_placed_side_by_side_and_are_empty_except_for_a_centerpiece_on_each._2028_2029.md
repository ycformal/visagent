Question: Two identical dining tables, each with chairs arranged for seating at least four, are placed side by side and are empty except for a centerpiece on each.

Reference Answer: True

Left image URL: http://www.homebunch.com/wp-content/uploads/69.png

Right image URL: http://3.bp.blogspot.com/-vZdYGe9dBx8/T5BjWGlATfI/AAAAAAAASCM/3cicJmyBwFk/s1600/sweaks2.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are there two identical dining tables, each with chairs arranged for seating at least four, placed side by side and are empty except for a centerpiece on each?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are there two identical dining tables, each with chairs arranged for seating at least four, placed side by side and are empty except for a centerpiece on each?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there two identical dining tables, each with chairs arranged for seating at least four, placed side by side and are empty except for a centerpiece on each?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

