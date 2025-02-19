Question: What is sitting next to the chair?

Reference Answer: flowers

Image path: ./sampled_GQA/n6908.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is sitting next to the chair?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

