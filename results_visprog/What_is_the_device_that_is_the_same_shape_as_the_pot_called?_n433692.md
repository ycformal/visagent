Question: What is the device that is the same shape as the pot called?

Reference Answer: The device is a computer mouse.

Image path: ./sampled_GQA/n433692.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pot')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the device that is the same shape as the pot called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='pot')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the device that is the same shape as the pot called?')=<b><span style='color: green;'>scale</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>scale</span></b></div><hr>

Answer: scale
