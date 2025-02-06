Question: Does the door next to the garage look modern and shut?

Reference Answer: yes

Image path: ./sampled_GQA/n210269.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='garage')
IMAGE0=CROP_NEXTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='door')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Does the door look modern and shut?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTOF'

