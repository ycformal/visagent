Question: What color do you think the jacket that the man is wearing is?

Reference Answer: The jacket is green.

Image path: ./sampled_GQA/2398108.jpg

Program:

```
 What color is A wearing?
Program:
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the jacket that the man is wearing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='man')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the jacket that the man is wearing?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>black</span></b></div><hr>

Answer: black
