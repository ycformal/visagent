Question: What is the color of the chair?

Reference Answer: The chair is brown.

Image path: ./sampled_GQA/n207708.jpg

Program:

```
 What is <attr> of A?
Program:
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the color of the chair?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='chair')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the color of the chair?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>white</span></b></div><hr>

Answer: white
