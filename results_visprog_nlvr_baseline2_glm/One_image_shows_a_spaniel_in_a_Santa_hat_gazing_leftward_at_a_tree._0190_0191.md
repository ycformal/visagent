Question: One image shows a spaniel in a Santa hat gazing leftward at a tree.

Reference Answer: False

Left image URL: http://www.warrenphotographic.co.uk/photography/bigs/17117-Sleepy-American-Cocker-Spaniel-pup-with-Santa-hat-on-white-background.jpg

Right image URL: https://i.pinimg.com/736x/02/01/df/0201df5fc2835973b2dd0c46f869b404--christmas-friends-christmas-dog.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a spaniel in a Santa hat gazing leftward at a tree.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a spaniel in a Santa hat gazing leftward at a tree.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

