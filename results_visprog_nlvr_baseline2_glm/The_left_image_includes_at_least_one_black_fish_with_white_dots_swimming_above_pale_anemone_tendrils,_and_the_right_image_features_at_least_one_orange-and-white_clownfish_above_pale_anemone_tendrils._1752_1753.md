Question: The left image includes at least one black fish with white dots swimming above pale anemone tendrils, and the right image features at least one orange-and-white clownfish above pale anemone tendrils.

Reference Answer: True

Left image URL: https://t4.ftcdn.net/jpg/01/14/40/07/240_F_114400728_HQRqEByDeiUSKH0S44n0w1BDC4DjsdU0.jpg

Right image URL: https://images.robertharding.com/preview/RM/RH/HORIZONTAL/1159-283.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left image includes at least one black fish with white dots swimming above pale anemone tendrils, and the right image features at least one orange-and-white clownfish above pale anemone tendrils.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image includes at least one black fish with white dots swimming above pale anemone tendrils, and the right image features at least one orange-and-white clownfish above pale anemone tendrils.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

