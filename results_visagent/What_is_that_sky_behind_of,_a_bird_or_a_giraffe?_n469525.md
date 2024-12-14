Question: What is that sky behind of, a bird or a giraffe?

Reference Answer: The sky is behind a giraffe.

Image path: ./sampled_GQA/n469525.jpg

Program:

```
 What is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='sky')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='bird')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='giraffe')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE0,question='What is that sky behind of, a bird or a giraffe?')
ANSWER1=EVAL(expr="'bird' if {ANSWER0} in {IMAGE1} else 'giraffe' if {ANSWER0} in {IMAGE2} else 'none'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: giraffe

