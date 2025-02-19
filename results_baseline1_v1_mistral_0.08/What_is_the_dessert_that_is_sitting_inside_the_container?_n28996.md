Question: What is the dessert that is sitting inside the container?

Reference Answer: brownie

Image path: ./sampled_GQA/n28996.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='container')
IMAGE0=CROP_INSIDE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the dessert?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_INSIDE'

