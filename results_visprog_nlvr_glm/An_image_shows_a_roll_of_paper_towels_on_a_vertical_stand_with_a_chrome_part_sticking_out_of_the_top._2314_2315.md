Question: An image shows a roll of paper towels on a vertical stand with a chrome part sticking out of the top.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/ca/fc/d9/cafcd9dadf0ca3057444ec732ec7729f--paper-towels-toilet-paper.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/30/b7/38/30b738c6e4aba44a11531d7396c968e9.jpg

Program:

```
Statement: An image shows a roll of paper towels on a vertical stand with a chrome part sticking out of the top.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a roll of paper towels on a vertical stand?')
ANSWER1=VQA(image=RIGHT,question='Is there a roll of paper towels on a vertical stand?')
ANSWER2=VQA(image=LEFT,question='Is there a chrome part sticking out of the top?')
ANSWER3=VQA(image=RIGHT,question='Is there a chrome part sticking out of the top?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Answer: Runtime error: 'An'

