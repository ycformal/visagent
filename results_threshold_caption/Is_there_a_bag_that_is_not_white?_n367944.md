Question: Is there a bag that is not white?

Reference Answer: No, there is a bag but it is white.

Image path: ./sampled_GQA/n367944.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bag')
ANSWER0=VQA(image=IMAGE,question='What color is the bag?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='bag')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the bag?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'white' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'white' != 'white' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
