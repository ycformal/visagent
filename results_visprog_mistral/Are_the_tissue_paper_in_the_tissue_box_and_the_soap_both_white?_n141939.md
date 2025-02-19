Question: Are the tissue paper in the tissue box and the soap both white?

Reference Answer: yes

Image path: ./sampled_GQA/n141939.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='tissue box')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='tissue paper')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='soap')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='What color is the tissue paper?')
ANSWER1=VQA(image=IMAGE2,question='What color is the soap?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'white' and {ANSWER1} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: Coordinate 'right' is less than 'left'

