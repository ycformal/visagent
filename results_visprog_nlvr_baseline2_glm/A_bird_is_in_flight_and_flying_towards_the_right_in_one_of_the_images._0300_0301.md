Question: A bird is in flight and flying towards the right in one of the images.

Reference Answer: False

Left image URL: https://t1.pixers.pics/img/wall-murals-brightly-colored-rainbow-lorikeet.jpg?H4sIAAAAAAAAA3WO627DIAyFXwekNHYo1zxA__YRIgqkY80FAVunPX2Jqv2crCPbRzr-DF9bsXMAF7YaMqzR-yXAHJe2lTGHEn8DwU4hp2NzF4KIdNy_Q3Z5T-SkdXdIGXaIjk_bgqvND_JRayojQDn3Kf60a625Am4twHBQgBKEEdxyNmvnjZqqTaHa0-Npfba1T9u9w6Po3xscseMHvua4kvbP3kiVfKY7hX9o7xlaCi5XkAhSgJbAzWFNl6tEKbTkZlLKD4xbtGa-qSBMODNtjNKeoXA3P_SN8gIBod0lLAEAAA==

Right image URL: https://photos.smugmug.com/Animals/Bird-Animal-Pictures/Lorikeet-Wildlife-Photography/i-SD8twGv/0/650a9291/S/Lorikeet%2000001%20Two%20lorikeets%20sit%20on%20a%20branch%2C%20by%20Peter%20J%20Mancus-S.jpg

Original program:

```
Statement: A bird is in flight and flying towards the right in one of the images.
Program:
ANSWER0=VQA(image=LEFT,question='Is the bird in flight?')
ANSWER1=VQA(image=RIGHT,question='Is the bird in flight?')
ANSWER2=VQA(image=LEFT,question='Is the bird flying towards the right?')
ANSWER3=VQA(image=RIGHT,question='Is the bird flying towards the right?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A bird is in flight and flying towards the right in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A bird is in flight and flying towards the right in one of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

