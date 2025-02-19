Question: Are there paintings on the front of the school in the image?

Reference Answer: yes

Image path: ./sampled_GQA/n346247.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='school')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='paintings')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

