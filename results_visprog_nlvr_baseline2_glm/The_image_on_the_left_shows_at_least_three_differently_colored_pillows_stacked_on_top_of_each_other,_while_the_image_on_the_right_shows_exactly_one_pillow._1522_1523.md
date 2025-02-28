Question: The image on the left shows at least three differently colored pillows stacked on top of each other, while the image on the right shows exactly one pillow.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2016/10/04/18/3060403A00000578-3820398-image-m-35_1475600472217.jpg

Right image URL: http://c.shld.net/rpx/i/s/pi/mp/7019/prod_3436139302?src=http%3A%2F%2Fwww.vminnovations.com%2Fsys%2Fresource.ashx%3Fguid%3Dce1d56c3c0314c469978eb9978ee858e%26x%3D.jpg%26s%3D501&d=14ca92c21fd47cd6150438e3ecd3ade1e10f2ee7&hei=333&wid=333&op_sharpen=1

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
ANSWER0=VQA(image=IMAGE,question="Is 'The image on the left shows at least three differently colored pillows stacked on top of each other, while the image on the right shows exactly one pillow.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The image on the left shows at least three differently colored pillows stacked on top of each other, while the image on the right shows exactly one pillow.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

