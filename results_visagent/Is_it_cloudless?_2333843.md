Question: Is it cloudless?

Reference Answer: Yes, it is cloudless.

Image path: ./sampled_GQA/2333843.jpg

Program:

```
 Is A <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'cloudless' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>sunny</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'cloudless' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'sunny' == 'cloudless' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
