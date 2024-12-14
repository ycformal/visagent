Question: Is it a vanilla frosting?

Reference Answer: Yes, that is a vanilla frosting.

Image path: ./sampled_GQA/2411734.jpg

Program:

```
 Is it A <type>?
Program:
ANSWER0=VQA(image=IMAGE,question='Is it a vanilla frosting?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is it a vanilla frosting?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

