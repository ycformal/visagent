Question: Does the cabinet to the left of the other cabinet look clean?

Reference Answer: yes

Image path: ./sampled_GQA/n97485.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinet')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cabinet')
ANSWER0=VQA(image=IMAGE1,question='Does this cabinet look clean?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'IMAGE1'

