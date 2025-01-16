Question: What is the color of the traffic light that is not short?

Reference Answer: The traffic light is black.

Image path: ./sampled_GQA/n116329.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='traffic light')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='short')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What color is the traffic light?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: green

