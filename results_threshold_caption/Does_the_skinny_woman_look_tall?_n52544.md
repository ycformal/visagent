Question: Does the skinny woman look tall?

Reference Answer: No, the woman is short.

Image path: ./sampled_GQA/n52544.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='skinny woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Does the skinny woman look tall?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='skinny woman')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the skinny woman look tall?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
