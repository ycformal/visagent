Question: Is there a clock that is not made of wood?

Reference Answer: No, there is a clock but it is made of wood.

Image path: ./sampled_GQA/2348624.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='clock')
ANSWER0=VQA(image=IMAGE,question='What material is the clock made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'wood' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='clock')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the clock made of?')=<b><span style='color: green;'>metal</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'wood' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'metal' != 'wood' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
