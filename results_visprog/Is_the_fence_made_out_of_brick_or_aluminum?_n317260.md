Question: Is the fence made out of brick or aluminum?

Reference Answer: The fence is made of aluminum.

Image path: ./sampled_GQA/n317260.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fence')
ANSWER0=VQA(image=IMAGE,question='What material is the fence made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brick' or {ANSWER0} == 'aluminum' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='fence')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the fence made of?')=<b><span style='color: green;'>metal</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'brick' or ANSWER0 == 'aluminum' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'metal' == 'brick' or 'metal' == 'aluminum' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
