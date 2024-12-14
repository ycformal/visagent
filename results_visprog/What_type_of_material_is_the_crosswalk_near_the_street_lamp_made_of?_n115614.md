Question: What type of material is the crosswalk near the street lamp made of?

Reference Answer: The crosswalk is made of cement.

Image path: ./sampled_GQA/n115614.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='street lamp')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='crosswalk')
ANSWER0=VQA(image=IMAGE0,question='What type of material is the crosswalk?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEAR'

