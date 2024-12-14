Question: What is the name of the sign that is made of the same material as the vehicle on the right of the picture?

Reference Answer: The sign is a traffic sign.

Image path: ./sampled_GQA/n486200.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='RIGHT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='vehicle')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE,object='sign')
IMAGE2=CROP_SAME_MATERIAL(image=IMAGE,box=BOX2,reference_image=IMAGE1)
ANSWER0=VQA(image=IMAGE2,question='What is the name of the sign?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_SAME_MATERIAL'

