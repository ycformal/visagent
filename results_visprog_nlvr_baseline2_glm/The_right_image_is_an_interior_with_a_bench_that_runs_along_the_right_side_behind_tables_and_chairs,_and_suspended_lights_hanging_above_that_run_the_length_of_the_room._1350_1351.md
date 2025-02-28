Question: The right image is an interior with a bench that runs along the right side behind tables and chairs, and suspended lights hanging above that run the length of the room.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/0e/92/ce/0e92cec64efc8dca117017f1ab3b5c24--ramen-restaurant-restaurant-ideas.jpg

Right image URL: https://i.pinimg.com/564x/77/72/a6/7772a69c4e416b3ccbb2f7852eab9ccd--small-restaurant-design-modern-restaurant.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image is an interior with a bench that runs along the right side behind tables and chairs, and suspended lights hanging above that run the length of the room.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image is an interior with a bench that runs along the right side behind tables and chairs, and suspended lights hanging above that run the length of the room.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

