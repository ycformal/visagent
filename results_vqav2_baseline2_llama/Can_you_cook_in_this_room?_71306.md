Question: Can you cook in this room?

Reference Answer: yes

Image path: ./sampled_GQA/71306.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='kitchen')
ANSWER0=VQA(image=IMAGE,question='Can you cook in this room?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Can you cook in this room?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you cook in this room?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

