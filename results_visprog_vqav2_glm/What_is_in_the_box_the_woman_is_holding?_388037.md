Question: What is in the box the woman is holding?

Reference Answer: donuts

Image path: ./sampled_GQA/388037.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='woman')
IMAGE0=CROP_WHATISIN(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is in the box the woman is holding?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_WHATISIN'

