Question: All watercraft shown are riderless and sitting in water.

Reference Answer: True

Left image URL: http://lightweightboatbuilding.com/images/arrow/0.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/b7/7d/9b/b77d9be8ba442673c6b1ea632093dbc9.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All watercraft shown are riderless and sitting in water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All watercraft shown are riderless and sitting in water.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

