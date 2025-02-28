Question: Two dogs are near green vegetation.

Reference Answer: False

Left image URL: https://get.pxhere.com/photo/white-puppy-dog-animal-cute-pet-fur-brown-mammal-spaniel-close-up-whiskers-vertebrate-funny-dog-breed-cavalier-king-charles-spaniel-king-charles-spaniel-dog-like-mammal-carnivoran-kooikerhondje-welsh-springer-spaniel-phalene-736286.jpg

Right image URL: http://buzzsharer.com/wp-content/uploads/2015/08/Cavalier-King-Charles-Spaniel-face-closeup.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Two dogs are near green vegetation.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two dogs are near green vegetation.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

