Question: Is this a chocolate ice cream?

Reference Answer: No, this is a vanilla ice cream.

Image path: ./sampled_GQA/n312206.jpg

Program:

```
 Is A <object>?
Program:
ANSWER0=VQA(image=IMAGE,question='Is this a chocolate ice cream?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is this a chocolate ice cream?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if False else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
