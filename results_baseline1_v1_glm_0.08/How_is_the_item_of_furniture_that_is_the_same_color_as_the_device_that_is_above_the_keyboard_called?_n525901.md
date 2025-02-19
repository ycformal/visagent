Question: How is the item of furniture that is the same color as the device that is above the keyboard called?

Reference Answer: office chair

Image path: ./sampled_GQA/n525901.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='keyboard')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_BELOW(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE1,object='item of furniture')
ANSWER0=VQA(image=IMAGE2,question='How is the item of furniture that is the same color as the {object} called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE2'

