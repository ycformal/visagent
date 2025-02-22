Question: An image shows one boat with orange-red sail near a row of no more than six white-sailed boats.

Reference Answer: True

Left image URL: https://afloat.ie/images/news_content_images/yawls_racing11.jpg

Right image URL: https://lh3.googleusercontent.com/Je0WMcgCQYy8Zn2Cl0WOz5Ebk73cZmAkXgPATkJ5dtFgOs4kAEwBYZmchsyVo5KrhjqVU1mWkyN8NNvT5u9cCv_Z8ezqhr-vN5m1FdRPxGA51Lv24ajuS9oLJPfztPIdDMIpVcZF-BMi94C-ZaNkSbep7mF82diXCO6dqqYhIhA3vmPO7WiRzF-p4Qb8sqPr0xejsWaVDuk1-UJOkdW7kh9RpMG6W9Zhr2WnYuUVeNx1wRsk17YjOnkIR9tKKCGPKy261pU2RmspMuvD2spp_EQr7q3lW0w97xAEHSFR7gHfT4jxf_y2VX3y3mo8kW60UofqBDUEt9fBrQQ82sj5LR9Lnj1PRCob9lm3q8CiBMk0N4pEM_EoevwUimHSDdoWR5ChbHoDA9RHAFlhNdBQ_219A_3fKJhiJJTi31tIgXwDD3OymvZ1oFdpEEnxEMmN3whoAOSGhAnIfU6bZTJjoRlbfXEKo7Yj-RKQMDcp-r3Zg3mAfhcjgVfufnfAmcD9LM2VIvqayyCIS6u0rQLHIveyv3Gp7rqPxJsoswyd3PjkYVVuZ_PEKrWgOAZ2mjO2aIdG8pYVTYH2k_LwihT-6fvWWtt9g5M=w1000-h850-no

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

