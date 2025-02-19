Question: What's in front of the cabinet?

Reference Answer: table

Image path: ./sampled_GQA/n65885.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cabinet')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is in front of the cabinet?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: runtime error

