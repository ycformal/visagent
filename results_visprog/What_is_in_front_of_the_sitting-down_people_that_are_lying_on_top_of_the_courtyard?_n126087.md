Question: What is in front of the sitting-down people that are lying on top of the courtyard?

Reference Answer: The rackets are in front of the people.

Image path: ./sampled_GQA/n126087.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='courtyard')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sitting-down people')
IMAGE1=CROP_ONTOP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='front')
ANSWER0=VQA(image=IMAGE1,question='What is in front of the sitting-down people?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_ONTOP'

