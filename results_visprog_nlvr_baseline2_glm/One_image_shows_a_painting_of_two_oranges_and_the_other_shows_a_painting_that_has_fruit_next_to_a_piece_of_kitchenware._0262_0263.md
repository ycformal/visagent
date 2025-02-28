Question: One image shows a painting of two oranges and the other shows a painting that has fruit next to a piece of kitchenware.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/a0/e7/31/a0e731adbb824aba5b871e88cde49db2.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/4a/68/0b/4a680bbbf7d8d0e7d5af752b843ee46d.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a painting of two oranges and the other shows a painting that has fruit next to a piece of kitchenware.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a painting of two oranges and the other shows a painting that has fruit next to a piece of kitchenware.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

