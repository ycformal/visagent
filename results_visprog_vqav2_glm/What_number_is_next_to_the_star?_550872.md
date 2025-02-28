Question: What number is next to the star?

Reference Answer: 9

Image path: ./sampled_GQA/550872.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='star')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What number is next to the star?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_NEXTTO'

