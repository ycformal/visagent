Question: Are there any traffic lights in the picture?

Reference Answer: Yes, there is a traffic light.

Image path: ./sampled_GQA/n486200.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='traffic light')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='traffic light')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>19</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 19 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.
