Question: Where are the menu?

Reference Answer: on table

Image path: ./sampled_GQA/442161.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='menu')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

