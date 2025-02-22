Question: There are exactly two bunches of attached balloons.

Reference Answer: False

Left image URL: https://www.tuscanyballooning.com/wordpress/wp-content/uploads/2016/02/group-of-hot-air-balloons-takeoff-in-formation.jpg

Right image URL: https://images.freeimages.com/images/premium/large-thumbs/1203/12038329-happy-young-girl-holding-a-bunch-of-balloons-outside.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

