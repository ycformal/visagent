Question: Is the faucet in front of the white tiles?

Reference Answer: yes

Image path: ./sampled_GQA/n386682.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='faucet')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='white tiles')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

