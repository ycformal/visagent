Question: Is there a plate in the photograph?

Reference Answer: Yes, there is a plate.

Image path: ./sampled_GQA/n170941.jpg

Program:

```
Is A in the image?
Program:
BOX0=LOC(image=IMAGE,object='plate')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='plate')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>4</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 4 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
