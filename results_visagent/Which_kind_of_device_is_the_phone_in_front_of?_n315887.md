Question: Which kind of device is the phone in front of?

Reference Answer: The phone is in front of the computer.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
What kind of device is A in front of?
Program:
BOX0=LOC(image=IMAGE,object='phone')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='all')
IMAGE1=CROP_FRONT(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What kind of device is the phone in front of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: phone

