Question: At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/91IXOx-2g-L._SL1500_.jpg

Right image URL: http://www.pbs.org/wgbh/nova/next/wp-content/uploads/2017/03/bed-net-2048x1152.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one person can be seen lying in bed in one image and there is nobody in a bed in the other image.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

