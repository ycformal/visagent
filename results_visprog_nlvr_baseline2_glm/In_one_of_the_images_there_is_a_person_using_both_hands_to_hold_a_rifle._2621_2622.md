Question: In one of the images there is a person using both hands to hold a rifle.

Reference Answer: True

Left image URL: https://media1.s-nbcnews.com/j/newscms/2014_44/740391/141029-wild-hog-1020a_bc9361e525e737f838450fc275cc432b.nbcnews-fp-1240-520.jpg

Right image URL: https://lh3.googleusercontent.com/-kV-5h9XqzQ4/VuvvsfWAPsI/AAAAAAAAGik/l9mDJJKE3AIH9UuapvLo717VXOYqfjnjQCHMYBhgL/s1600/P1080185.JPG

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one of the images there is a person using both hands to hold a rifle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one of the images there is a person using both hands to hold a rifle.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

