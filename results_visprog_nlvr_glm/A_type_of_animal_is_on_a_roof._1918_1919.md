Question: A type of animal is on a roof.

Reference Answer: False

Left image URL: http://3.bp.blogspot.com/-vcQiBsj8THw/Vb304GcUdBI/AAAAAAAALP4/tNUFmI0j1fE/s1600/P1080673.jpg

Right image URL: http://members.madasafish.com/~cj_whitehound/Fanfic/map_of_Hogwarts/artwork/Gearranan.jpg

Program:

```
Statement: A type of animal is on a roof.
Program:
ANSWER0=VQA(image=LEFT,question='Is there an animal on the roof?')
ANSWER1=VQA(image=RIGHT,question='Is there an animal on the roof?')
ANSWER2=EVAL(expr='{ANSWER0} or {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'A'

