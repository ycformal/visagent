Question: Is the mirror on the left side of the photo?

Reference Answer: no

Image path: ./sampled_GQA/n209843.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='mirror')
ANSWER0=EVAL(expr="'yes' if {BOX0}.x < IMAGE.width/2 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the mirror on the left side of the photo?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the mirror on the left side of the photo?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

