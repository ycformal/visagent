Question: In at least one image there is a house facing forward left with metal door windows.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/a8/25/e4/a825e4a37dbce1b050902233cf9b74ae--thatched-roof-stone-cottages.jpg

Right image URL: https://i.pinimg.com/736x/6c/e6/03/6ce6036d908644d8d195e319f40137cd--thatched-roof-english-cottages.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a house facing forward left with metal door windows.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a house facing forward left with metal door windows.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

