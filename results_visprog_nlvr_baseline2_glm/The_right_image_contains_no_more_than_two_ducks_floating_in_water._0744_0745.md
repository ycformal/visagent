Question: The right image contains no more than two ducks floating in water.

Reference Answer: False

Left image URL: http://www.northescambia.com/wp-content/uploads/2007/12/geese12.jpg

Right image URL: http://www.croydonducks.co.uk/parks-2016/csam_1399.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains no more than two ducks floating in water.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains no more than two ducks floating in water.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

