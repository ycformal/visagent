Question: What is the name of the piece of furniture that is made of the same material as the door?

Reference Answer: The piece of furniture is a drawer.

Image path: ./sampled_GQA/2369861.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the door made of?')
ANSWER1=VQA(image=IMAGE,question='What is the name of the piece of furniture that is made of {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='door')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the door made of?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the piece of furniture that is made of {ANSWER0}?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>wood</span></b></div><hr>

Answer: wood
