Question: The dumbbells in the image on the right are shown in a variety of colors.

Reference Answer: True

Left image URL: https://i.ebayimg.com/00/s/NzY4WDEwMjQ=/z/tVwAAOSwSypY92Wj/$_86.JPG

Right image URL: http://1.bp.blogspot.com/-AMTRpoKmVNs/VU0sEQmgPOI/AAAAAAAAHdw/mJ-9BmuS2tk/s1600/IMG_0068.JPG

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The dumbbells in the image on the right are shown in a variety of colors.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dumbbells in the image on the right are shown in a variety of colors.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

