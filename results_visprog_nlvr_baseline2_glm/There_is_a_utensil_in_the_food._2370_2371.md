Question: There is a utensil in the food.

Reference Answer: False

Left image URL: https://www.simplyquinoa.com/wp-content/uploads/2016/08/vegan-cheesy-zucchini-noodles-6.jpg

Right image URL: https://i.pinimg.com/736x/45/b8/2b/45b82b854e0ac47f2e3b610d60d45e9c--creamy-chicken-piccata-recipe-chicken-piccata-pasta.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a utensil in the food.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a utensil in the food.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

