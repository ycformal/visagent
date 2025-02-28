Question: Do the buildings have a lot of windows?

Reference Answer: yes

Image path: ./sampled_GQA/46603.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='buildings')
ANSWER0=VQA(image=IMAGE,question='How many windows do the buildings have?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 10 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
BOX0=LOC(image=IMAGE,object='buildings',plural=True)
ANSWER0=VQA(image=IMAGE,question='How many windows do the buildings have?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 10 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

