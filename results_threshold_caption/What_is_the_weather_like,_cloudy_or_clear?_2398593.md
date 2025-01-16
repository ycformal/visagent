Question: What is the weather like, cloudy or clear?

Reference Answer: It is clear.

Image path: ./sampled_GQA/2398593.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'cloudy' if {ANSWER0} == 'cloudy' else 'clear'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>clear</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'cloudy' if ANSWER0 == 'cloudy' else 'clear'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'cloudy' if 'clear' == 'cloudy' else 'clear'")=<b><span style='color: green;'>clear</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>clear</span></b></div><hr>

Answer: clear

