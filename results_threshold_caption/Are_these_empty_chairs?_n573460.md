Question: Are these empty chairs?

Reference Answer: Yes, these are empty chairs.

Image path: ./sampled_GQA/n573460.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='chair')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>93</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 93 == 0 else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
