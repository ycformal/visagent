Question: One bookstore image shows a staircase to a second floor.

Reference Answer: False

Left image URL: http://www.ohiobookstore.net/images/store_front.jpg

Right image URL: https://i1.ypcdn.com/blob/56e8d28a17dc04c41b1858501e275f6ce8c77f66_400x260_crop.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

