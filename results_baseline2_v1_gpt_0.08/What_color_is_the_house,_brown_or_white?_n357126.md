Question: What color is the house, brown or white?

Reference Answer: brown

Image path: ./sampled_GQA/n357126.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What color is the house?')
ANSWER1=EVAL(expr="'brown' if {ANSWER0} == 'brown' else 'white'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What color is the house?')
ANSWER1=EVAL(expr="'brown' if {ANSWER0} == 'brown' else 'white'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the house?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'brown' if ANSWER0 == 'brown' else 'white'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'brown' if 'white' == 'brown' else 'white'")=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>white</span></b></div><hr>

Answer: white

