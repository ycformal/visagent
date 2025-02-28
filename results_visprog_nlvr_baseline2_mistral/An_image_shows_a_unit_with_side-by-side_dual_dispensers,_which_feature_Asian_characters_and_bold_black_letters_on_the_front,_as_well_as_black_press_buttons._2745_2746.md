Question: An image shows a unit with side-by-side dual dispensers, which feature Asian characters and bold black letters on the front, as well as black press buttons.

Reference Answer: False

Left image URL: https://ae01.alicdn.com/kf/HTB1F2xbMXXXXXaDXXXXq6xXFXXX6/Simple-Wall-mounted-font-b-three-b-font-colors-hotel-toilet-bathroom-manual-350ML-ABS-Soap.jpg

Right image URL: https://i.pinimg.com/736x/cb/e8/ce/cbe8ce93389cf07d217c35a1b91bdb55--shampoo-dispenser-hotel-soap.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a unit with side-by-side dual dispensers?')
ANSWER1=VQA(image=RIGHT,question='Does the image show a unit with side-by-side dual dispensers?')
ANSWER2=VQA(image=LEFT,question='Do the dispensers feature Asian characters and bold black letters on the front?')
ANSWER3=VQA(image=RIGHT,question='Do the dispensers feature Asian characters and bold black letters on the front?')
ANSWER4=VQA(image=LEFT,question='Do the dispensers have black press buttons?')
ANSWER5=VQA(image=RIGHT,question='Do the dispensers have black press buttons?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a unit with side-by-side dual dispensers, which feature Asian characters and bold black letters on the front, as well as black press buttons.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a unit with side-by-side dual dispensers, which feature Asian characters and bold black letters on the front, as well as black press buttons.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

