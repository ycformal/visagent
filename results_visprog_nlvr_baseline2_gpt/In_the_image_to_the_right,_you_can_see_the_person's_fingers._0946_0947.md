Question: In the image to the right, you can see the person's fingers.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/EyVXlVFA_-I/hqdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/2a/b4/11/2ab411151cb378fa17b76d8b1bf9bccb.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Can you see the person's fingers in the image?')
FINAL_ANSWER=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In the image to the right, you can see the person's fingers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the image to the right, you can see the person's fingers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

