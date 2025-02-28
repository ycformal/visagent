Question: Where is the pizza?

Reference Answer: on table

Image path: ./sampled_GQA/307166.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pizza')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

