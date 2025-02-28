Question: There are two canopies with at least one square one attached to the bed poles.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/5e/2d/57/5e2d57f3fc72e7bb14a775e174c35e86--mosquito-net-shay-mitchell.jpg

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51RyHFKKmaL._US500_.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two canopies with at least one square one attached to the bed poles.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two canopies with at least one square one attached to the bed poles.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

