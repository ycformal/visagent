Question: Is there a woman in this picture?

Reference Answer: Yes, there is a woman.

Image path: ./sampled_GQA/n71728.jpg

Program:

```
 Is A in this picture?
Program:
BOX0=LOC(image=IMAGE,object='woman')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='woman')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>18</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 18 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
