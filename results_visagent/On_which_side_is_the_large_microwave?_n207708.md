Question: On which side is the large microwave?

Reference Answer: The microwave is on the left of the image.

Image path: ./sampled_GQA/n207708.jpg

Program:

```
 On which side is A?
Program:
BOX0=LOC(image=IMAGE,object='large microwave')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='On which side is the large microwave?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='large microwave')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='On which side is the large microwave?')=<b><span style='color: green;'>right</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>right</span></b></div><hr>

Answer: right
