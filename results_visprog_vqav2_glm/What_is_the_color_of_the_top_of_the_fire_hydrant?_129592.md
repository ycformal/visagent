Question: What is the color of the top of the fire hydrant?

Reference Answer: red

Image path: ./sampled_GQA/129592.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fire hydrant')
IMAGE0=CROP_TOP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the top of the fire hydrant?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_TOP'

