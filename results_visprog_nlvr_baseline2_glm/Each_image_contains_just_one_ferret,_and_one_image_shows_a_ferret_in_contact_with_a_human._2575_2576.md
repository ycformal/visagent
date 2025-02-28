Question: Each image contains just one ferret, and one image shows a ferret in contact with a human.

Reference Answer: True

Left image URL: http://www.petsamaritans.co.uk/wp-content/uploads/2016/09/ferret-jingo-1-1.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/0d/02/7b/89/friendly-ferret.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains just one ferret, and one image shows a ferret in contact with a human.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains just one ferret, and one image shows a ferret in contact with a human.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

