Question: Is the weather cloudy?

Reference Answer: No, it is clear.

Image path: ./sampled_GQA/2399616.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'cloudy' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>clear</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'cloudy' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'clear' == 'cloudy' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

