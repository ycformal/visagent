Question: Is there any bag that is black?

Reference Answer: No, there is a bag but it is red.

Image path: ./sampled_GQA/n16378.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bag')
ANSWER0=VQA(image=IMAGE,question='What color is the bag?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'black' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bag')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the bag?')=<b><span style='color: green;'>red</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'black' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'red' == 'black' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No
