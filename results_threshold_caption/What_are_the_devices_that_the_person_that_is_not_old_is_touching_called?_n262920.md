Question: What are the devices that the person that is not old is touching called?

Reference Answer: The devices are laptops.

Image path: ./sampled_GQA/n262920.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
BOX2=LOC(image=IMAGE0,object='old')
IMAGE1=CROP_NOT(image=IMAGE0,box=BOX2)
ANSWER0=VQA(image=IMAGE1,question='What are the devices that the person is touching called?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: laptop

