Question: What type of vehicle is made of the same material as the motorbike that is parked along the sidewalk?

Reference Answer: The car is made of the same material as the motorbike.

Image path: ./sampled_GQA/n131634.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='motorbike')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the motorbike made of?')
BOX1=LOC(image=IMAGE,object='sidewalk')
IMAGE1=CROP_ALONG(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='vehicle')
ANSWER1=VQA(image=IMAGE1,question='What type of vehicle is it?')
ANSWER2=EVAL(expr="'{ANSWER1}' if {ANSWER0} in {ANSWER1} else 'unknown'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: motorcycle

