Question: Does the weather appear to be sunny today?

Reference Answer: Yes, it is sunny.

Image path: ./sampled_GQA/2376413.jpg

Program:

```
 Is A <attr> today?
Program:
ANSWER0=VQA(image=IMAGE,question='Does the weather appear to be sunny today?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the weather appear to be sunny today?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

