Question: Is this a skateboarder or a snowboarder?

Reference Answer: This is a skateboarder.

Image path: ./sampled_GQA/n460556.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='skateboarder')
BOX1=LOC(image=IMAGE,object='snowboarder')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'skateboarder' if {ANSWER0} > 0 else 'snowboarder' if {ANSWER1} > 0 else 'neither'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='skateboarder')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='snowboarder')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'skateboarder' if ANSWER0 > 0 else 'snowboarder' if ANSWER1 > 0 else 'neither'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'skateboarder' if 1 > 0 else 'snowboarder' if 1 > 0 else 'neither'")=<b><span style='color: green;'>skateboarder</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>skateboarder</span></b></div><hr>

Answer: skateboarder
