Question: The image on the right contains at least 1 balloon that hasn't been inflated.

Reference Answer: False

Left image URL: https://4.bp.blogspot.com/-xj5dSJfEZkE/VwoK5H2JJlI/AAAAAAAADZ0/oqVe49ZLhCgnW_UMVoiWrg4XDU-GFyPgg/s1600/water%2Bballoon%2B1.jpg

Right image URL: https://potreby-kancelarske.eu/balonek-20012-metaliza~nahled.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many balloons have been inflated?')
ANSWER1=EVAL(expr='{ANSWER0} < 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many balloons have been inflated?')
ANSWER1=EVAL(expr='{ANSWER0} < 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many balloons have been inflated?')=<b><span style='color: green;'>12</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 < 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="12 < 1")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

