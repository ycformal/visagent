Question: In at least one image there is at least one man sitting in a barber chair getting his head shaved.

Reference Answer: True

Left image URL: https://bloximages.newyork1.vip.townnews.com/lancasteronline.com/content/tncms/assets/v3/editorial/0/9c/09cd2602-b0b8-11e6-a570-9f5ed1b6c855/5834493679cfe.image.jpg?resize=1200%2C792

Right image URL: https://i1.ypcdn.com/blob/46ace786ab71a4e711668048114eebe088e9c2ec_400x260_crop.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is at least one man sitting in a barber chair getting his head shaved.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is at least one man sitting in a barber chair getting his head shaved.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

