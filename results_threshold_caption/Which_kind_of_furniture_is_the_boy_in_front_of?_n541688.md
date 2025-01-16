Question: Which kind of furniture is the boy in front of?

Reference Answer: The boy is in front of the table.

Image path: ./sampled_GQA/n541688.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='boy')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Which kind of furniture is the boy in front of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: table

