Question: Each image contains just one beagle puppy, who is posed on a draped black cloth.

Reference Answer: True

Left image URL: http://www.beaglespocket.com/uploads/8/6/8/6/8686937/4051816_orig.jpg

Right image URL: http://www.tinybeagles.com/uploads/8/6/8/6/8686937/1110605_orig.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains just one beagle puppy, who is posed on a draped black cloth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains just one beagle puppy, who is posed on a draped black cloth.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

