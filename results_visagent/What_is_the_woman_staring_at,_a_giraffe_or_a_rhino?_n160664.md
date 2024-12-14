Question: What is the woman staring at, a giraffe or a rhino?

Reference Answer: The woman is staring at a giraffe.

Image path: ./sampled_GQA/n160664.jpg

Program:

```
 What is the woman staring at, A or B?
Program:
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='giraffe')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='rhino')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE0,question='What is the woman staring at, a giraffe or a rhino?')
ANSWER1=EVAL(expr="'giraffe' if {ANSWER0} == {IMAGE1} else 'rhino'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: giraffe

