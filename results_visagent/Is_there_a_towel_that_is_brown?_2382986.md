Question: Is there a towel that is brown?

Reference Answer: Yes, there is a towel that is brown.

Image path: ./sampled_GQA/2382986.jpg

Program:

```
 Is there A that is <attr>?
Program:
BOX0=LOC(image=IMAGE,object='towel')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the towel?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='towel')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the towel?')=<b><span style='color: green;'>brown</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'brown' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'brown' == 'brown' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
