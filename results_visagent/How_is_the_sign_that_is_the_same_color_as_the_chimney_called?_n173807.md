Question: How is the sign that is the same color as the chimney called?

Reference Answer: The sign is a street sign.

Image path: ./sampled_GQA/n173807.jpg

Program:

```
 How is A that is the same <attr> as B called?
Program:
BOX0=LOC(image=IMAGE,object='chimney')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='sign')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the chimney?')
ANSWER1=VQA(image=IMAGE1,question='What color is the sign?')
ANSWER2=EVAL(expr="'The sign that is the same color as the chimney is called a {ANSWER1}'.format(ANSWER1={ANSWER0})")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: chimney
