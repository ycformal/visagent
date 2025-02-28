Question: Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.

Reference Answer: False

Left image URL: http://www.sheprescue.org/images/harley%20von%20hena%201.JPG

Right image URL: http://www.freedoglistings.co.uk/pics/puppies-breeders-rescue_uk/014512_6FC_The-best-Temprement--eating-a-bone.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains one dog, with the one on the left posed with front paws forward, and the dog on the right showing some teeth.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

