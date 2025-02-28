Question: there is a staircase with a window on the wall and a light hanging from the ceiling

Reference Answer: False

Left image URL: http://www.bloominghomestead.com/wp-content/uploads/2016/04/Easy-Banister-Makeover.jpg

Right image URL: https://st.hzcdn.com/simgs/e15158a00258114e_4-8568/eclectic-staircase.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'there is a staircase with a window on the wall and a light hanging from the ceiling' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there is a staircase with a window on the wall and a light hanging from the ceiling' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

