Question: Several boats are in the water in the image on the left.

Reference Answer: True

Left image URL: https://afloat.ie/images/news_content_images/yawls_racing11.jpg

Right image URL: https://lh3.googleusercontent.com/Je0WMcgCQYy8Zn2Cl0WOz5Ebk73cZmAkXgPATkJ5dtFgOs4kAEwBYZmchsyVo5KrhjqVU1mWkyN8NNvT5u9cCv_Z8ezqhr-vN5m1FdRPxGA51Lv24ajuS9oLJPfztPIdDMIpVcZF-BMi94C-ZaNkSbep7mF82diXCO6dqqYhIhA3vmPO7WiRzF-p4Qb8sqPr0xejsWaVDuk1-UJOkdW7kh9RpMG6W9Zhr2WnYuUVeNx1wRsk17YjOnkIR9tKKCGPKy261pU2RmspMuvD2spp_EQr7q3lW0w97xAEHSFR7gHfT4jxf_y2VX3y3mo8kW60UofqBDUEt9fBrQQ82sj5LR9Lnj1PRCob9lm3q8CiBMk0N4pEM_EoevwUimHSDdoWR5ChbHoDA9RHAFlhNdBQ_219A_3fKJhiJJTi31tIgXwDD3OymvZ1oFdpEEnxEMmN3whoAOSGhAnIfU6bZTJjoRlbfXEKo7Yj-RKQMDcp-r3Zg3mAfhcjgVfufnfAmcD9LM2VIvqayyCIS6u0rQLHIveyv3Gp7rqPxJsoswyd3PjkYVVuZ_PEKrWgOAZ2mjO2aIdG8pYVTYH2k_LwihT-6fvWWtt9g5M=w1000-h850-no

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Are there several boats in the water?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there several boats in the water?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

