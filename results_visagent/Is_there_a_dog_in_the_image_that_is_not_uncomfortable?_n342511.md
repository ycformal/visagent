Question: Is there a dog in the image that is not uncomfortable?

Reference Answer: No, there is a dog but it is uncomfortable.

Image path: ./sampled_GQA/n342511.jpg

Program:

```
 Is there A in the image that is not <attr>?
Program:
BOX0=LOC(image=IMAGE,object='dog')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the dog uncomfortable?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'no' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='dog')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog uncomfortable?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'no' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if False == 'no' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: Yes
