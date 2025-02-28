Question: One image shows a reptilian creature emerging from its green scene on a flat TV screen.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/9STBsPHIEPA/maxresdefault.jpg

Right image URL: https://i.pinimg.com/736x/56/a1/07/56a107de3e0538c876c857d281cc9c04--viera-panasonic-televisions.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a reptilian creature emerging from its green scene on a flat TV screen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a reptilian creature emerging from its green scene on a flat TV screen.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

