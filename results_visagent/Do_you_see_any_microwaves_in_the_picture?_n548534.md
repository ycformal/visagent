Question: Do you see any microwaves in the picture?

Reference Answer: Yes, there is a microwave.

Image path: ./sampled_GQA/n548534.jpg

Program:

```
Do you see any A in the picture?
Program:
BOX0=LOC(image=IMAGE,object='microwave')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='microwave')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 4 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
