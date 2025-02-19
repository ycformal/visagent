Question: Are there any people next to the vehicle that is yellow and black?

Reference Answer: yes

Image path: ./sampled_GQA/n406334.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle',attributes='yellow and black')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='people')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

