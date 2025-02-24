Question: What is the name of the item of furniture that is the same color as the door that is not short?

Reference Answer: bookcase

Image path: ./sampled_GQA/n207708.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='door')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='furniture')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='door')
IMAGE2=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='furniture')
ANSWER0=VQA(image=IMAGE0,question='What color is the door?')
ANSWER1=VQA(image=IMAGE1,question='What color is the furniture?')
ANSWER2=VQA(image=IMAGE2,question='What color is the door?')
ANSWER3=VQA(image=IMAGE3,question='What color is the furniture?')
ANSWER4=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} and {ANSWER2}!= {ANSWER3} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Answer: Runtime error: 'IMAGE3'

