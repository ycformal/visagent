Question: Why is the surfboard there?

Reference Answer: to surf

Image path: ./sampled_GQA/204329.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the surfboard there?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Why is the surfboard there?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Why is the surfboard there?')=<b><span style='color: green;'>to dry</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>to dry</span></b></div><hr>

Answer: to dry

