Question: Is there any speaker in the picture that is not white?

Reference Answer: No, there is a speaker but it is white.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='speaker')
ANSWER0=VQA(image=IMAGE,question='What color is the speaker?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='speaker')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the speaker?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'white' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'black' != 'white' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
