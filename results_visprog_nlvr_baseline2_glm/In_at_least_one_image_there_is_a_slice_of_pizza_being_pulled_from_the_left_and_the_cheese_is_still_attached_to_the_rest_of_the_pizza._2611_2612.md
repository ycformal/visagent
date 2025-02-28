Question: In at least one image there is a slice of pizza being pulled from the left and the cheese is still attached to the rest of the pizza.

Reference Answer: True

Left image URL: https://s3-media2.fl.yelpcdn.com/bphoto/rksezBzZeg5ONDvcqb8QWg/o.jpg

Right image URL: http://cdn.foodbeast.com.s3.amazonaws.com/content/uploads/2014/03/Double-Pepperoni-Papa-Johns.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a slice of pizza being pulled from the left and the cheese is still attached to the rest of the pizza.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a slice of pizza being pulled from the left and the cheese is still attached to the rest of the pizza.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

