Question: What appliance is sitting in front of the wall?

Reference Answer: stove

Image path: ./sampled_GQA/n280089.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_INFRONT_OF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
ANSWER0=VQA(image=IMAGE0,question='What appliance is sitting in front of the wall?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_INFRONT_OF'

