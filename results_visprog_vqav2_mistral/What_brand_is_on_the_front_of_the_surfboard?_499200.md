Question: What brand is on the front of the surfboard?

Reference Answer: rip curl

Image path: ./sampled_GQA/499200.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='surfboard')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What brand is on the front of the surfboard?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

