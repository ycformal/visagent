Question: What kind of device is made of the same material as the device above the desk?

Reference Answer: computer monitor

Image path: ./sampled_GQA/n398257.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='desk')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_ABOVE(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='device')
ANSWER0=VQA(image=IMAGE2,question='What kind of device is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE2'

