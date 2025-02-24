Question: Do you see instruments next to the fireplace?

Reference Answer: yes

Image path: ./sampled_GQA/n302387.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fireplace')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='instruments')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes, there are instruments next to the fireplace.

