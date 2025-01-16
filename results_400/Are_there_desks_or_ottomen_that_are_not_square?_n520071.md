Question: Are there desks or ottomen that are not square?

Reference Answer: No, there is a desk but it is square.

Image path: ./sampled_GQA/n520071.jpg

Chain:

```
LOC(desk)
LOC(ottomen)->NOT->SHAPE(square)
```
Program:

```
BOX0=LOC(image=IMAGE,object='desk')
BOX1=LOC(image=IMAGE,object='ottomen')
IMAGE0=CROP(image=IMAGE,box=BOX1)
IMAGE1=CROP(image=IMAGE0,box=BOX1)
```
Answer: Cannot be determined.

