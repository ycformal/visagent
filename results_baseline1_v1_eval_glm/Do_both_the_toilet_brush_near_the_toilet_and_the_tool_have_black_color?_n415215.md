Question: Do both the toilet brush near the toilet and the tool have black color?

Reference Answer: yes

Image path: ./sampled_GQA/n415215.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='toilet brush')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='toilet')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='tool')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE0,question='What color is the toilet brush?')
ANSWER1=VQA(image=IMAGE2,question='What color is the tool?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'black' and {ANSWER1} == 'black' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'CROP_NEAR'

