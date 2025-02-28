Question: One boat has unfurled white sails, and the other has furled white sails.

Reference Answer: False

Left image URL: http://www.tallship-fan.de/images/rr2015_0757.jpg

Right image URL: http://www.tallship-fan.de/images/rr2015_0237.jpg

Original program:

```
The program provided does not have a statement or a program to evaluate.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One boat has unfurled white sails, and the other has furled white sails.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One boat has unfurled white sails, and the other has furled white sails.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

