Question: One image shows a baby cheetah alone on green grass, and the other image shows a baby cheetah standing with its front paws on a reclining adult cheetah.

Reference Answer: False

Left image URL: https://c2.staticflickr.com/4/3796/8754290777_72bfbf83b7_b.jpg

Right image URL: https://media1.s-nbcnews.com/i/newscms/2016_36/1156726/dog-cheetah-today-160908-tease_b95774caf4ca1eecfc4df641d8feddd0.jpg

Original program:

```
Statement: One image shows a baby cheetah alone on green grass, and the other image shows a baby cheetah standing with its front paws on a reclining adult cheetah.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a baby cheetah alone on green grass, and the other image shows a baby cheetah standing with its front paws on a reclining adult cheetah.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a baby cheetah alone on green grass, and the other image shows a baby cheetah standing with its front paws on a reclining adult cheetah.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

