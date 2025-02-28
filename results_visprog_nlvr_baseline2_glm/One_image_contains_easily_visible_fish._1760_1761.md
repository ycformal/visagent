Question: One image contains easily visible fish.

Reference Answer: False

Left image URL: http://www.habitas.org.uk/marinelife/cnidaria/stococs.jpg

Right image URL: https://i.ytimg.com/vi/xovtWqygix0/maxresdefault.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains easily visible fish.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains easily visible fish.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

