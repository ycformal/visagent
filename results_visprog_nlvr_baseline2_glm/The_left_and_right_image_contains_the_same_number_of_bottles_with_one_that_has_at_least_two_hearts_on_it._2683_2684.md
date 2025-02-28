Question: The left and right image contains the same number of bottles with one that has at least two hearts on it.

Reference Answer: True

Left image URL: https://i5.walmartimages.com/asr/a410fc42-96be-4749-b117-b6a4709cd631_1.eb2044bb6e8f53eb4c9376add4b9adad.jpeg?odnHeight=450&odnWidth=450&odnBg=FFFFFF

Right image URL: https://i.ebayimg.com/00/s/MTYwMFgxNjAw/z/E-QAAOSwmblZ2Wq5/$_58.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of bottles with one that has at least two hearts on it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of bottles with one that has at least two hearts on it.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

