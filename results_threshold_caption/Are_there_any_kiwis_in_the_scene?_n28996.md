Question: Are there any kiwis in the scene?

Reference Answer: No, there are no kiwis.

Image path: ./sampled_GQA/n28996.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='kiwi')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='kiwi')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 0 > 0 else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
