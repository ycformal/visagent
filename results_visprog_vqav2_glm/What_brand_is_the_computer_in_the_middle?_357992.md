Question: What brand is the computer in the middle?

Reference Answer: apple

Image path: ./sampled_GQA/357992.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='computer')
IMAGE0=CROP_MIDDLE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What brand is the computer?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_MIDDLE'

