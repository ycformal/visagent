Question: Does that dome look yellow?

Reference Answer: Yes, the dome is yellow.

Image path: ./sampled_GQA/713731.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='dome')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the dome?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'yellow' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='dome')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the dome?')=<b><span style='color: green;'>yellow and red</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'yellow' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'yellow and red' == 'yellow' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
