Question: There is a bottle of hot sauce that was previously opened and used.

Reference Answer: True

Left image URL: https://images.heb.com/is/image/HEBGrocery/prd-small/boar-s-head-jalapeno-pepper-sauce-000581096.jpg

Right image URL: http://2.bp.blogspot.com/-up7r1yifiCs/UPlFA7AAyLI/AAAAAAAAC7Q/F4FSD3i_Xq8/s1600/2013-01-17+13.16.50.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is a bottle of hot sauce that was previously opened and used.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a bottle of hot sauce that was previously opened and used.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

