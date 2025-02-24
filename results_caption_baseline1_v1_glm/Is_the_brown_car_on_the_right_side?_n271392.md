Question: Is the brown car on the right side?

Reference Answer: yes

Image path: ./sampled_GQA/n271392.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='car')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the car?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'brown' and else 'no'")
ANSWER2=EVAL(expr="'yes' if {ANSWER1} == 'yes' and else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: invalid syntax (<string>, line 1)

