Question: Are the planes planning to land soon?

Reference Answer: yes

Image path: ./sampled_GQA/62685.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Are the planes planning to land soon?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Are the planes planning to land soon?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the planes planning to land soon?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

