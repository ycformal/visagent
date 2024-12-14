Question: How is the item of furniture that is made of same material as the fan on the ceiling called?

Reference Answer: The piece of furniture is a table.

Image path: ./sampled_GQA/n192021.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fan')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What material is the fan made of?')
BOX1=LOC(image=IMAGE,object='furniture')
IMAGE1=CROP_SAMEMATERIAL(image=IMAGE,box=BOX1,material=ANSWER0)
ANSWER1=VQA(image=IMAGE1,question='What is the name of the furniture?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_SAMEMATERIAL'

