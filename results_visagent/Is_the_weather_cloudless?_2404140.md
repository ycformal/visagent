Question: Is the weather cloudless?

Reference Answer: No, it is cloudy.

Image path: ./sampled_GQA/2404140.jpg

Program:

```
 Is A <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'cloudless' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>overcast</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'cloudless' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'overcast' == 'cloudless' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

