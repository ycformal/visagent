Question: Are there any bears?

Reference Answer: Yes, there is a bear.

Image path: ./sampled_GQA/2320680.jpg

Program:

```
Are there any A?
Program:
BOX0=LOC(image=IMAGE,object='bear')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bear')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 4 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
