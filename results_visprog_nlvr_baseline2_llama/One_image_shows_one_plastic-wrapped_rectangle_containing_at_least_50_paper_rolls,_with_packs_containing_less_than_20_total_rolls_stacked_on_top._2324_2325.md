Question: One image shows one plastic-wrapped rectangle containing at least 50 paper rolls, with packs containing less than 20 total rolls stacked on top.

Reference Answer: True

Left image URL: https://sc01.alicdn.com/kf/HTB1utE1FFXXXXcBaFXXq6xXFXXXx/200339910/HTB1utE1FFXXXXcBaFXXq6xXFXXXx.jpg

Right image URL: https://sc01.alicdn.com/kf/HTB1JkN_LVXXXXclXFXX760XFXXXb/wholesale-bulk-toilet-tissue-soft-paper-with.png

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many paper rolls are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many paper rolls are in the image?')
ANSWER2=VQA(image=LEFT,question='Is the rectangle plastic-wrapped?')
ANSWER3=VQA(image=RIGHT,question='Is the rectangle plastic-wrapped?')
ANSWER4=VQA(image=LEFT,question='Are there less than 20 paper rolls in the image?')
ANSWER5=VQA(image=RIGHT,question='Are there less than 20 paper rolls in the image?')
ANSWER6=VQA(image=LEFT,question='Are there at least 50 paper rolls in the image?')
ANSWER7=VQA(image=RIGHT,question='Are there at least 50 paper rolls in the image?')
ANSWER8=EVAL(expr='{ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER3} and {ANSWER5} and {ANSWER7}')
ANSWER10=EVAL(expr='{ANSWER8} xor {ANSWER9}')
FINAL_ANSWER=RESULT(var=ANS
```
Answer: True

