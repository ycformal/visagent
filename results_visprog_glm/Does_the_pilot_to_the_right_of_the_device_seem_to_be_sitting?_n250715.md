Question: Does the pilot to the right of the device seem to be sitting?

Reference Answer: yes

Image path: ./sampled_GQA/n250715.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='RIGHT')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='device')
IMAGE1=CROP_LEFTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='pilot')
ANSWER0=VQA(image=IMAGE2,question='Does this person seem to be sitting?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE2'

