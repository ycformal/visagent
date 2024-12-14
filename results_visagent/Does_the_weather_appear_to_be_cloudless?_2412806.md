Question: Does the weather appear to be cloudless?

Reference Answer: Yes, it is cloudless.

Image path: ./sampled_GQA/2412806.jpg

Program:

```
Does A appear to be <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='Does the weather appear to be cloudless?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the weather appear to be cloudless?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

