Question: The left image features a blond girl in a pink tank top that covers her midriff standing in front of at least one person and posing with a red dumbbell in each hand, lifted with the elbow forming a right angle.

Reference Answer: True

Left image URL: https://marketplace.canva.com/MAA8BQVtJZM/1/screen/canva-group-of-smiling-people-working-out-with-dumbbells-MAA8BQVtJZM.jpg

Right image URL: https://st2.depositphotos.com/1046535/7980/i/950/depositphotos_79806238-stock-photo-fitness-people-in-gym-working.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image features a blond girl in a pink tank top that covers her midriff standing in front of at least one person and posing with a red dumbbell in each hand, lifted with the elbow forming a right angle.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image features a blond girl in a pink tank top that covers her midriff standing in front of at least one person and posing with a red dumbbell in each hand, lifted with the elbow forming a right angle.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

