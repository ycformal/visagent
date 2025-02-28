Question: All the cars are facing towards the left.

Reference Answer: True

Left image URL: https://images.honestjohn.co.uk/imagecache/file/fit/730x700/media/3437537/Saab~9-3~Convertible~(3).jpg

Right image URL: http://images.parkers.bauercdn.com/gallery-image/pagefiles/202331/static-exterior/1752x1168/1200797.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All the cars are facing towards the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All the cars are facing towards the left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

