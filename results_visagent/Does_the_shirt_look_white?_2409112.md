Question: Does the shirt look white?

Reference Answer: No, the shirt is blue.

Image path: ./sampled_GQA/2409112.jpg

Program:

```
Does A look <attr>?
Program:
BOX0=LOC(image=IMAGE,object='shirt')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the shirt?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='shirt')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the shirt?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'white' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'black' == 'white' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
