Question: Is the weather cloudy?

Reference Answer: yes

Image path: ./sampled_GQA/n494677.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='clouds')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the weather cloudy?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the weather cloudy?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes.

