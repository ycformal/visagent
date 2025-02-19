Question: What do you think is parked in front of the fire truck that is shown in the photograph?

Reference Answer: car

Image path: ./sampled_GQA/n480253.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fire truck')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What do you think is parked in front of the fire truck?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

