Question: An image shows a three-colored hound standing with its body in profile and its white-tipped tail raised.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/8b/11/6c/8b116c4abe7f9889ef90e08c9de35dae--priscilla-presley--year-olds.jpg

Right image URL: https://i.pinimg.com/736x/10/d0/7c/10d07c8b2aad2ec2836371fc8270768e---year-olds--years.jpg

Original program:

```
Statement: An image shows a three-colored hound standing with its body in profile and its white-tipped tail raised.
Program:
ANSWER0=VQA(image=LEFT,question='Is the hound three-colored?')
ANSWER1=VQA(image=RIGHT,question='Is the hound three-colored?')
ANSWER2=VQA(image=LEFT,question='Is the hound standing with its body in profile?')
ANSWER3=VQA(image=RIGHT,question='Is the hound standing with its body in profile?')
ANSWER4=VQA(image=LEFT,question='Is the hound's tail white-tipped?')
ANSWER5=VQA(image=RIGHT,question='Is the hound's tail white-tipped?')
ANSWER6=VQA(image=LEFT,question='Is the hound's tail raised?')
ANSWER7=VQA(image=RIGHT,question='Is the hound's tail raised?')
ANSWER8=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5} and {
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a three-colored hound standing with its body in profile and its white-tipped tail raised.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a three-colored hound standing with its body in profile and its white-tipped tail raised.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

