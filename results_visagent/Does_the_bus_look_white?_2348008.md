Question: Does the bus look white?

Reference Answer: No, the bus is orange.

Image path: ./sampled_GQA/2348008.jpg

Program:

```
Does A look <attr>?
Program:
BOX0=LOC(image=IMAGE,object='bus')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the bus?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bus')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the bus?')=<b><span style='color: green;'>yellow</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'white' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'yellow' == 'white' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
