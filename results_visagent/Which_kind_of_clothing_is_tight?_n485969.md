Question: Which kind of clothing is tight?

Reference Answer: The clothing is pants.

Image path: ./sampled_GQA/n485969.jpg

Program:

```
Which kind of <attr> is A?
Program:
ANSWER0=VQA(image=IMAGE,question='Which kind of clothing is tight?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which kind of clothing is tight?')=<b><span style='color: green;'>pants</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>pants</span></b></div><hr>

Answer: pants
