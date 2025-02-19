Question: Do the metal utensils next to the forks look hard?

Reference Answer: yes

Image path: ./sampled_GQA/n479092.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='forks')
IMAGE0=CROP_NEXTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='metal utensils')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Do the metal utensils look hard?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTOF'

