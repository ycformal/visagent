Question: Which color are the small rocks that are lying on top of the ground?

Reference Answer: brown

Image path: ./sampled_GQA/n335542.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='ground')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='rocks')
ANSWER0=VQA(image=IMAGE0,question='What color are the small rocks that are lying on top of the ground?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOPOF'

