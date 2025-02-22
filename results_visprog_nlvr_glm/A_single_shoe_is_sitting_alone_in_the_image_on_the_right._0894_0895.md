Question: A single shoe is sitting alone in the image on the right.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/47/d3/27/47d327f049081e75733a7ce9e594ef16.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/2e/ae/61/2eae613bb39fe7e5f121975d654b97a4.jpg

Program:

```
Statement: A single shoe is sitting alone in the image on the right.
Program:
ANSWER0=VQA(image=RIGHT,question='How many shoes are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'A'

