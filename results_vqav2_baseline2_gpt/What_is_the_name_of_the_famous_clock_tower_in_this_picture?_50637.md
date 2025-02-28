Question: What is the name of the famous clock tower in this picture?

Reference Answer: big ben

Image path: ./sampled_GQA/50637.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is the name of the famous clock tower in this picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the name of the famous clock tower in this picture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the famous clock tower in this picture?')=<b><span style='color: green;'>big ben</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>big ben</span></b></div><hr>

Answer: Big Ben

