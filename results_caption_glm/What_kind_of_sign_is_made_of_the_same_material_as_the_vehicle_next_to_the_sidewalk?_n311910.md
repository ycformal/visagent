Question: What kind of sign is made of the same material as the vehicle next to the sidewalk?

Reference Answer: street sign

Image path: ./sampled_GQA/n311910.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='vehicle')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='sign')
ANSWER0=VQA(image=IMAGE0,question='What material is the {sign} made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

