Question: Is the umpire on the right?

Reference Answer: No, the umpire is on the left of the image.

Image path: ./sampled_GQA/n481655.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='umpire')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='RIGHT')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='umpire')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='RIGHT')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 1 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
