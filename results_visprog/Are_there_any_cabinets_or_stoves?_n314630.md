Question: Are there any cabinets or stoves?

Reference Answer: No, there are no cabinets or stoves.

Image path: ./sampled_GQA/n314630.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinet')
BOX1=LOC(image=IMAGE,object='stove')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='cabinet')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='stove')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 + ANSWER1 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 1 + 2 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
