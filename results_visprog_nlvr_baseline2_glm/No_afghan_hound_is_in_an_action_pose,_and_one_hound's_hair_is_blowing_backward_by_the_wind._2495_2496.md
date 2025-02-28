Question: No afghan hound is in an action pose, and one hound's hair is blowing backward by the wind.

Reference Answer: False

Left image URL: http://www.afghanhoundpedigrees.com/pics/medium/677/med_5589ac124ee7f.jpg

Right image URL: https://i.pinimg.com/736x/ec/ec/ac/ececac722a3a4ded9e7ff9ac9167a6ed--hound-puppies-hound-dog.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'No afghan hound is in an action pose, and one hound's hair is blowing backward by the wind.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'No afghan hound is in an action pose, and one hound's hair is blowing backward by the wind.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

