Question: What kind of furniture is made of the same material as the frame?

Reference Answer: The end table is made of the same material as the frame.

Image path: ./sampled_GQA/2385070.jpg

Program:

```
What kind of <object> is made of the same <attr> as A?
Program:
BOX0=LOC(image=IMAGE,object='frame')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the frame made of?')
ANSWER1=VQA(image=IMAGE,question='What kind of furniture is made of {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='frame')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the frame made of?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What kind of furniture is made of {ANSWER0}?')=<b><span style='color: green;'>sofa</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>sofa</span></b></div><hr>

Answer: sofa
