Question: Is it cloudy?

Reference Answer: No, it is clear.

Image path: ./sampled_GQA/n272313.jpg

Program:

```
 Is A <attr>?
Program:
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'cloudy' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>sunny</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'cloudy' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'sunny' == 'cloudy' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
