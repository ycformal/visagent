Question: Is there a bag in this image that is black?

Reference Answer: No, there is a bag but it is blue.

Image path: ./sampled_GQA/2359489.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bag')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the bag?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'black' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bag')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the bag?')=<b><span style='color: green;'>blue</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'black' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'blue' == 'black' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
