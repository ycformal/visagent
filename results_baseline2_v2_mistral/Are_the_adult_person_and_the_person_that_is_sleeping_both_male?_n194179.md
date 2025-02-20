Question: Are the adult person and the person that is sleeping both male?

Reference Answer: yes

Image path: ./sampled_GQA/n194179.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='adult person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='person that is sleeping')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='Is the adult person male?')
ANSWER1=VQA(image=IMAGE1,question='Is the person that is sleeping male?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'yes' and {ANSWER1} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Are the adult person and the person that is sleeping both male?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are the adult person and the person that is sleeping both male?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: No

