Question: Is there a chair next to the cupboard?

Reference Answer: yes

Image path: ./sampled_GQA/n283587.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cupboard')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: "runtime error"

