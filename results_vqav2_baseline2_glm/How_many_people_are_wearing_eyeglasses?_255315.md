Question: How many people are wearing eyeglasses?

Reference Answer: 1

Image path: ./sampled_GQA/255315.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='How many people are wearing eyeglasses?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='How many people are wearing eyeglasses?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many people are wearing eyeglasses?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

