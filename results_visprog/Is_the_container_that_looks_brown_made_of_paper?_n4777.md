Question: Is the container that looks brown made of paper?

Reference Answer: Yes, the paper container is made of paper.

Image path: ./sampled_GQA/n4777.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='container')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the container?')
ANSWER1=VQA(image=IMAGE0,question='What material is the container made of?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'brown' and {ANSWER1} == 'paper' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='container')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the container?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What material is the container made of?')=<b><span style='color: green;'>plastic</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'brown' and ANSWER1 == 'paper' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'white' == 'brown' and 'plastic' == 'paper' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
