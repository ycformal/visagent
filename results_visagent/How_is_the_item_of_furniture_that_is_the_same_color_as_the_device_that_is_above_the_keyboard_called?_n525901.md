Question: How is the item of furniture that is the same color as the device that is above the keyboard called?

Reference Answer: The piece of furniture is an office chair.

Image path: ./sampled_GQA/n525901.jpg

Program:

```
 How is the <attr> of A that is the same <attr> as B called?
Program:
BOX0=LOC(image=IMAGE,object='keyboard')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the keyboard?')
BOX1=LOC(image=IMAGE,object='device')
IMAGE1=CROP_ABOVE(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What color is the device?')
BOX2=LOC(image=IMAGE,object='furniture')
IMAGE2=CROP_SAMECOLOR(image=IMAGE,box1=BOX0,box2=BOX1)
ANSWER2=VQA(image=IMAGE2,question='How is the item of furniture that is the same color as the device that is above the keyboard called?')
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: desk

