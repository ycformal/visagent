Question: What is placed next to the bus on the right?

Reference Answer: car

Image path: ./sampled_GQA/203294.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='RIGHT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bus')
IMAGE1=CROP_NEXTTO(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is placed next to the bus?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

