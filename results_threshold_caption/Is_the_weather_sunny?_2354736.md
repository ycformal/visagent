Question: Is the weather sunny?

Reference Answer: Yes, it is sunny.

Image path: ./sampled_GQA/2354736.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the weather like?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'sunny' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the weather like?')=<b><span style='color: green;'>sunny</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'sunny' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'sunny' == 'sunny' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

