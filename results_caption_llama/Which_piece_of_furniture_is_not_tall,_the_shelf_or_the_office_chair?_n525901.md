Question: Which piece of furniture is not tall, the shelf or the office chair?

Reference Answer: office chair

Image path: ./sampled_GQA/n525901.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='shelf')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='office chair')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='shelf')
IMAGE2=CROP(image=IMAGE,box=BOX2)
BOX3=LOC(image=IMAGE2,object='office chair')
ANSWER0=VQA(image=IMAGE0,question='What is the height of the shelf?')
ANSWER1=VQA(image=IMAGE1,question='What is the height of the office chair?')
ANSWER2=VQA(image=IMAGE2,question='What is the height of the shelf?')
ANSWER3=VQA(image=IMAGE3,question='What is the height of the office chair?')
ANSWER4=EVAL(expr="'shelf' if {ANSWER0} < {ANSWER1} and {ANSWER2} < {ANSWER3} else 'office chair'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Answer: runtime error

