Question: Is there a fence in front of the trees?

Reference Answer: No, there is a boy in front of the trees.

Image path: ./sampled_GQA/n494918.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='trees')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='fence')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'
