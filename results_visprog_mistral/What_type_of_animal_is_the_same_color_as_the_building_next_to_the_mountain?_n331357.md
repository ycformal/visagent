Question: What type of animal is the same color as the building next to the mountain?

Reference Answer: calf

Image path: ./sampled_GQA/n331357.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mountain')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='building')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the building?')
ANSWER1=VQA(image=IMAGE,question='What type of animal is {ANSWER0}?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEXTTO'

