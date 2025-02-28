Question: What are the women walking beside?

Reference Answer: building

Image path: ./sampled_GQA/135281.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='women')
IMAGE0=CROP_BESIDE(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What are the women walking beside?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_BESIDE'

