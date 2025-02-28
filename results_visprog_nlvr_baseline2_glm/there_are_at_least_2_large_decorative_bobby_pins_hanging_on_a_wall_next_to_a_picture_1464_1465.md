Question: there are at least 2 large decorative bobby pins hanging on a wall next to a picture

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/c4/ab/6a/c4ab6a966ace6f97289df97fa5afd785--new-baby-gifts-safety-pins.jpg

Right image URL: https://www.deepuddy.co.uk/wp-content/uploads/2014/05/PuddyDee290420141142-e14002497924661.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'there are at least 2 large decorative bobby pins hanging on a wall next to a picture' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there are at least 2 large decorative bobby pins hanging on a wall next to a picture' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

