Question: In front of what's the jar?

Reference Answer: The jar is in front of the paper towels.

Image path: ./sampled_GQA/n578564.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='jar')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='In front of what?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

