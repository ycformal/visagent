Question: What is the person that is standing doing?

Reference Answer: The snowboarder is riding.

Image path: ./sampled_GQA/n369970.jpg

Program:

```
 What is A doing?
Program:
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the person doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='person')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the person doing?')=<b><span style='color: green;'>snowboarding</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>snowboarding</span></b></div><hr>

Answer: snowboarding
