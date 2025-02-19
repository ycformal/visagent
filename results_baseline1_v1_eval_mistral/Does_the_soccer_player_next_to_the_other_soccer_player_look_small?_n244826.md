Question: Does the soccer player next to the other soccer player look small?

Reference Answer: yes

Image path: ./sampled_GQA/n244826.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='soccer player')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='soccer player')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Does the soccer player look small?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

