Question: Does the cat look comfortable?

Reference Answer: yes

Image path: ./sampled_GQA/137413.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Does the cat look comfortable?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Does the cat look comfortable?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the cat look comfortable?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

