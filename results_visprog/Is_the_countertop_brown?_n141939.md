Question: Is the countertop brown?

Reference Answer: Yes, the countertop is brown.

Image path: ./sampled_GQA/n141939.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='countertop')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the countertop?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='countertop')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the countertop?')=<b><span style='color: green;'>brown</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'brown' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'brown' == 'brown' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
