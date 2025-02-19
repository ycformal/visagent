Question: How is the item of furniture that is the same color as the device that is above the keyboard called?

Reference Answer: office chair

Image path: ./sampled_GQA/n525901.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='keyboard')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the device?')
IMAGE1=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE1,object=ANSWER0)
ANSWER1=VQA(image=IMAGE1,question='How is the item of furniture that is the same color as the device called?')
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: desk

