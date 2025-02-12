Question: What is the depth of the pot?

Reference Answer: deep

Image path: ./sampled_GQA/n184385.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pot')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=DEPTH(image=IMAGE0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'DEPTH'

