Question: Can you see the cat's stomach?

Reference Answer: yes

Image path: ./sampled_GQA/346112.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='cat')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='stomach')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Can you see the cat's stomach?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Can you see the cat's stomach?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

