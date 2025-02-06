Question: Do the metal utensils next to the forks look hard?

Reference Answer: yes

Image path: ./sampled_GQA/n479092.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='utensils')
IMAGE0=CROP_NEXTTO(image=IMAGE,object1=BOX0,object2='forks')
BOX1=LOC(image=IMAGE0,object='metal')
ANSWER0=VQA(image=IMAGE0,question='Do the metal utensils look hard?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

