Question: What kind of furniture is below the white thing that is in front of the monitor?

Reference Answer: The piece of furniture is a desk.

Image path: ./sampled_GQA/n315887.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='monitor')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white thing')
IMAGE1=CROP_BEHIND(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What kind of furniture is below the white thing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: desk

