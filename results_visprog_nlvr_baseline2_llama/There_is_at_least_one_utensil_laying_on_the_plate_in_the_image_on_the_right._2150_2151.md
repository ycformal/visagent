Question: There is at least one utensil laying on the plate in the image on the right.

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0d/98/32/3c/fried-chicken-creamed.jpg

Right image URL: https://s3-media3.fl.yelpcdn.com/bphoto/ApnO3bAsqWE5SLOjEyH8kQ/o.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many utensils are laying on the plate?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many utensils are laying on the plate?')
ANSWER1=EVAL(expr='{ANSWER0} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many utensils are laying on the plate?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="2 >= 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

