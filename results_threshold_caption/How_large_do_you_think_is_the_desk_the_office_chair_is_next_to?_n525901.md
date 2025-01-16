Question: How large do you think is the desk the office chair is next to?

Reference Answer: The desk is small.

Image path: ./sampled_GQA/n525901.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='office chair')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='desk')
ANSWER0=SIZE(box=BOX1)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: medium

