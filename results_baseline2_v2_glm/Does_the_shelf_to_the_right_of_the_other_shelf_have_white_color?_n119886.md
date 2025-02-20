Question: Does the shelf to the right of the other shelf have white color?

Reference Answer: yes

Image path: ./sampled_GQA/n119886.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='shelf')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='shelf')
ANSWER0=VQA(image=IMAGE1,question='What color is the shelf?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Does the shelf to the right of the other shelf have white color?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the shelf to the right of the other shelf have white color?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

