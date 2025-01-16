Question: Which kind of device is the phone in front of?

Reference Answer: The phone is in front of the computer.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='phone')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Which kind of device is this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: phone

