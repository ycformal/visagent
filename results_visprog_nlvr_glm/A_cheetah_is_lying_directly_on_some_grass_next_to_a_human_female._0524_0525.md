Question: A cheetah is lying directly on some grass next to a human female.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2014/08/11/1407750707175_wps_3_PIC_SHOWS_Meet_the_woman_.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2017/03/22/10/3E84DAEB00000578-4338262-image-a-11_1490179624697.jpg

Program:

```
Statement: A cheetah is lying directly on some grass next to a human female.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a cheetah lying on some grass?')
ANSWER1=VQA(image=RIGHT,question='Is there a cheetah lying on some grass?')
ANSWER2=VQA(image=LEFT,question='Is the cheetah next to a human female?')
ANSWER3=VQA(image=RIGHT,question='Is the cheetah next to a human female?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Answer: Runtime error: 'A'

