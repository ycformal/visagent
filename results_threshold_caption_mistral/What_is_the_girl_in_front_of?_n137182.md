Question: What is the girl in front of?

Reference Answer: trees

Image path: ./sampled_GQA/n137182.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='girl')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the girl in front of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: beach

