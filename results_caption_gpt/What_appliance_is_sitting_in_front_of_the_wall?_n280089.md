Question: What appliance is sitting in front of the wall?

Reference Answer: stove

Image path: ./sampled_GQA/n280089.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='wall')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What appliance is sitting in front of the wall?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: "runtime error"

