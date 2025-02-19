Question: Do you see any skateboarders or boys that are skating?

Reference Answer: yes

Image path: ./sampled_GQA/n65202.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='skateboard')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='boy')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='Are there any skateboarders?')
ANSWER1=VQA(image=IMAGE1,question='Are there any boys that are skating?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} > 0 or {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Do you see any skateboarders or boys that are skating?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Do you see any skateboarders or boys that are skating?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

