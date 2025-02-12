Question: Does the soccer player next to the other soccer player look small?

Reference Answer: yes

Image path: ./sampled_GQA/n244826.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='soccer player')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='soccer player')
ANSWER0=VQA(image=IMAGE0,question='How tall is the soccer player?')
ANSWER1=VQA(image=IMAGE,question='How tall is the other soccer player?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} < {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

