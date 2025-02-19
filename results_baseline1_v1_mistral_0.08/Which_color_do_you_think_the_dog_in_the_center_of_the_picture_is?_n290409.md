Question: Which color do you think the dog in the center of the picture is?

Reference Answer: light brown

Image path: ./sampled_GQA/n290409.jpg

Program:

```
BOX0=GET(image=IMAGE)
IMAGE0=CROP_CENTER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='dog')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Which color do you think the dog is?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_CENTER'

