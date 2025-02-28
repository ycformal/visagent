Question: What is the color of the nearest car?

Reference Answer: black

Image path: ./sampled_GQA/361142.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='car')
IMAGE0=CROP_NEAR(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the car?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEAR'

