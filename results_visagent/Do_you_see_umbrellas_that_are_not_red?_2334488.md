Question: Do you see umbrellas that are not red?

Reference Answer: Yes, there is a blue umbrella.

Image path: ./sampled_GQA/2334488.jpg

Program:

```
Do you see As that are not <attr>?
Program:
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the umbrella?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'red' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='umbrella')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the umbrella?')=<b><span style='color: green;'>blue</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'red' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'blue' != 'red' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
