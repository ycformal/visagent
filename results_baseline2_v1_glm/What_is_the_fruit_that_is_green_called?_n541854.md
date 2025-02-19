Question: What is the fruit that is green called?

Reference Answer: pear

Image path: ./sampled_GQA/n541854.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is the fruit that is green called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the fruit that is green called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the fruit that is green called?')=<b><span style='color: green;'>apple</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>apple</span></b></div><hr>

Answer: apple

