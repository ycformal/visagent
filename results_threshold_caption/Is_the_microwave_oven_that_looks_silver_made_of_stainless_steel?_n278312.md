Question: Is the microwave oven that looks silver made of stainless steel?

Reference Answer: Yes, the microwave oven is made of stainless steel.

Image path: ./sampled_GQA/n278312.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='microwave oven')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the microwave oven?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'silver' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='microwave oven')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the microwave oven?')=<b><span style='color: green;'>silver</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'silver' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'silver' == 'silver' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
