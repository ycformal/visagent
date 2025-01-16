Question: What device is the woman near the man holding?

Reference Answer: The woman is holding the camera.

Image path: ./sampled_GQA/n556604.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='man')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='woman')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What device is the woman holding?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: phone

