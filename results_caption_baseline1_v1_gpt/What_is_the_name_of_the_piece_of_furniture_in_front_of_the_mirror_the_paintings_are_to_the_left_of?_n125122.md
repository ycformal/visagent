Question: What is the name of the piece of furniture in front of the mirror the paintings are to the left of?

Reference Answer: bed

Image path: ./sampled_GQA/n125122.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mirror')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='paintings')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the name of the piece of furniture?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

