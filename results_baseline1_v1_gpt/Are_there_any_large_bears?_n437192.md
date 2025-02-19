Question: Are there any large bears?

Reference Answer: yes

Image path: ./sampled_GQA/n437192.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bear')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=FILTER(image=IMAGE0,object='bear',size='large')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'FILTER'

