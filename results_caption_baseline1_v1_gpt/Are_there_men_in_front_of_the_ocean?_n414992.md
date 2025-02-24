Question: Are there men in front of the ocean?

Reference Answer: yes

Image path: ./sampled_GQA/n414992.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='ocean')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='men')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes.

