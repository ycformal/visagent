Question: There are at least five people

Reference Answer: True

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0e/25/77/88/voronet-monastery-bucovina.jpg

Right image URL: http://theonearmedcrab.com/wp-content/uploads/2014/10/1409.21_132.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are at least five people' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are at least five people' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

