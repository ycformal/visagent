Question: An image contains exactly three bikini models, all standing, wearing sunglasses and facing forward.

Reference Answer: False

Left image URL: https://get.wallhere.com/photo/women-model-blonde-water-brunette-smiling-fashion-bikini-group-of-women-swimwear-clothing-supermodel-beauty-leg-photo-shoot-spring-break-309515.jpg

Right image URL: http://img.soy-chile.cl/Fotos/2015/01/12/file_20150112131300.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many bikini models are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many bikini models are in the image?')
ANSWER2=VQA(image=LEFT,question='Are all the bikini models standing?')
ANSWER3=VQA(image=RIGHT,question='Are all the bikini models standing?')
ANSWER4=VQA(image=LEFT,question='Are all the bikini models wearing sunglasses?')
ANSWER5=VQA(image=RIGHT,question='Are all the bikini models wearing sunglasses?')
ANSWER6=VQA(image=LEFT,question='Are all the bikini models facing forward?')
ANSWER7=VQA(image=RIGHT,question='Are all the bikini models facing forward?')
ANSWER8=EVAL(expr='{ANSWER0} == 3 and {ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER1} ==
```
Answer: false

