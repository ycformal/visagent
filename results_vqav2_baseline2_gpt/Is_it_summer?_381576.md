Question: Is it summer?

Reference Answer: no

Image path: ./sampled_GQA/381576.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What season is it?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'summer' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What season is it?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'summer' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What season is it?')=<b><span style='color: green;'>fall</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'summer' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'fall' == 'summer' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

