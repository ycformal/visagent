Question: What color is the jacket near the gloves?

Reference Answer: green

Image path: ./sampled_GQA/n317189.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='gloves')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the jacket?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEAR'

