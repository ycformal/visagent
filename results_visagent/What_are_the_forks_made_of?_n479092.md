Question: What are the forks made of?

Reference Answer: The forks are made of metal.

Image path: ./sampled_GQA/n479092.jpg

Program:

```
 What are A made of?
Program:
BOX0=LOC(image=IMAGE,object='forks')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What are the forks made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='forks')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What are the forks made of?')=<b><span style='color: green;'>metal</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>metal</span></b></div><hr>

Answer: metal
