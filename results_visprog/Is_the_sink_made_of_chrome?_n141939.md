Question: Is the sink made of chrome?

Reference Answer: No, the sink is made of porcelain.

Image path: ./sampled_GQA/n141939.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='sink')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the sink made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'chrome' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='sink')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the sink made of?')=<b><span style='color: green;'>porcelain</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'chrome' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'porcelain' == 'chrome' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
