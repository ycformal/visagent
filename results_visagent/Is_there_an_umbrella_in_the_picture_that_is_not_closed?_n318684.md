Question: Is there an umbrella in the picture that is not closed?

Reference Answer: Yes, there is a open umbrella.

Image path: ./sampled_GQA/n318684.jpg

Program:

```
 Is there A in the picture that is not <attr>?
Program:
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the umbrella closed?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'no' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='umbrella')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the umbrella closed?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'no' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if False == 'no' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: Yes.
