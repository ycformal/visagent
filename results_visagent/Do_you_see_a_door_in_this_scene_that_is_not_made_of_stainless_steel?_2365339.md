Question: Do you see a door in this scene that is not made of stainless steel?

Reference Answer: Yes, there are doors that are made of glass.

Image path: ./sampled_GQA/2365339.jpg

Program:

```
Do you see A that is not made of B?
Program:
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the door made of?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'stainless steel' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='door')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the door made of?')=<b><span style='color: green;'>glass</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'stainless steel' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'glass' != 'stainless steel' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
