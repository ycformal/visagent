Question: What type of vehicle is that goal in front of?

Reference Answer: The goal is in front of the car.

Image path: ./sampled_GQA/n259002.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='goal')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What type of vehicle is in front of the goal?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

