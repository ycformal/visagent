Question: Is the road wide and black?

Reference Answer: Yes, the road is wide and black.

Image path: ./sampled_GQA/n243701.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Is the road wide?')
ANSWER1=VQA(image=IMAGE,question='What color is the road?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'yes' and {ANSWER1} == 'black' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the road wide?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAGQASwMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AIZ/ilqmlagtnostjcWZTfueIt856jOR7VLF8a9fXb5lhprZAP3XX/2auG8MzXMuoi280hHIGQMEZ96szX2oS6m1tHKS6sIhnoTkKMn+dHWyFpud9bfGrVphKRollJ5QywSVwcZx71cX403qAmfwwwC43FZmGM/Va5rQbTULfXrZ5nt9isjOVjGTwSRnHqP0rLstY8VS6NJqUeqXP2eOTyzumJJOM96qcfZ2VTS4QTqJuCvY9Al+M1hPEYp9BlkRhyBODn81qqvjzwzOyqNKnQs6LhJwwO48jtyK4HV9autS8GW11fP50v8AaLRq7AZCiIHGQPU1n2JgEUN2ZSIYD86yPjPXBAHuRRyi9T0G68W+FXuFkjfU4NyZCoofaCMYyGHpXU6f8WfDMdrHBLJqBaNQC72/X8ia8csbmGyIS6gjleQBFkM6naBj+EA/nVa5WETFo1YRsQu3OTgH1qb2ZcYXV+x7zc/Efwk6Os1xKr7TjfbN6cc15ZD4ns4oVj+1xjaMYCH/AArH+0Wc0HkCEtI7cySA5QDtWXc20Ec7LGzMgxg/hSumEI3Zq+DYd2qRt51vEqorMZnCZAJ6E+9XriyvLbUJZbKXSrlid0ZMkWc7s4ySO1elHw7pJUI9kiqOAMZx/wCOVVl+Hvhq6Yk2yRs3UqxH9BU+0V7hymBplpqpunurm2U24i3iaMhgreWdy8E4AP8APvXmllqGoQ6fcQW7g28g/eLgEj3HpXr954YstJ09tTgmkE5jdGjLkjaIXA4z6AV4fAsluxePcFZdpOOCK0b5172o6c5Un7jtc3b87fAulL/f1G4b8kjH9ai0bSIL9ybq+EEKgMynHzcgYGT1qTVhs8GeH1Jxunu3/VB/StjRPh/4i1a0sriD7KlrcjzoPNlHzhcHkDOPxpyaRmtSSx8LJcK9xb3m2OBgf38QUt/u889O1Y0ozNzkgPuOO/NenS6X46i5k0TRbog5BjKKQfbpg1hQ+BvEME07/ZArmIqjbs4JGCRj8ayclc6KekJXMuw0mfVNIudRtyqFXKkOw+ZsZPJ7YqlFpTSRhnxuyQccjrWm+n6l4Ytba2v7Np42mMgiBxvONvX8a76HQtOs7eK2ht2kWJFUuSRuYD5j+LZq3ZamcHY0xrMUnEjk+wA/wqddRiJG3H4tiuWV2zgEGpBIwFLlRFy1qYlvfC8qQBXdbeUhVO5mJjcAAeuWrw1LLVbESQz2V1scYw8TDB/KvXrdgkY28HJJI+tUvFGo3Vv4avnguZo3CjayuQR8w6GqWgjjdS0HVb7wj4fNnpt1OsaXJfy4idpMvGR16CvXfDtq2m+HdNtCJI2ht1BU9VYjLfqTWRo2q3J0eyaaR5HMKbnLkk8dTmtVNUJIHmcns1TJcw07Gwtyy9wfqKf9uk7BP1FZEmqeRE8kuAiKWYkdAKp6V4lh1aKSRLWWII2396u3PuKjkRXMy5rmnprkcImEaPDIHWRc5wP4fpVxpJmYklMn/aaq/wBuiPVCPoaX7ZB/tflVcouYzdhUY8tCPcU2VY1TP2ck/wCwafHcK33sVKVVhxRYDBi3RxASo4POcfWuQ8Wfa7aS+ie4BhnjjkRWfJKkjAAzxgg16RKgCtnng14pqOoS6jFPPM5dzckpn+EY6D9Ke4LQ9L0O5SfRIXKlCiIqgnO4AYzVqVgybc9wao2FulnqiWtmfK3WccgjJJG48kjPr6Uatq39nyJHPBH5hGeu3I9SPzqKNVVIqS6mlemoSshby9Z2OniQqsq8uedq+1TaHAbW1myxd0kMJYk/MASRgfjWVaapZ3cF1bOGM0g8qIlf4s8EfQc1p6XPdSWIFztVgxA2ryQOM59TxVJNyuQ7KNjSa9iRsOwBpDfW+f8AWL+dQNkjkgj3FR7E/wCecf8A3zWyRmPSc8cmtCKY7F5rAjmUt9786tifA68VmWX9Tu/J0m7lJxshc5H0NeKi0mXSlnaJ/KM2Fkxwex/UGvXGxfxtZsFYTKUIfp+PtWV49WGy8G6fpsDDZFcRoMdWwrEsfck5qoxvqS5W0Kuk6kL7VrS6diJfK2SIEPyKoP51a8YLbyafHfgL5ok8mLDf6yILk7v88Uzw5AsSm5KlpFGxXfnaD1x6VzfxAvpodQtIYigjMLOFXPDE4P54FZUoRgrRWh0V6vtFHyVvxf8AmbEVrNpdwl1FaOySyKsYckbUZAdwOOeuK6PSbwSQTpcgCMznymPTHv3H1rmtc8TT3up2GnqvkLbwANsfG8sAOvYY4xWrDFJDYl3AwynaCCMGulpKld7s5G26mmyNaePYpdOVBwwJ5U+/t6GoNxqXT5y8NsZFGd5hfvuU/wCFRSqIZnjJOVJFZwk9mW0U8WqrlZJN3oVBqu9zLHyAQOxBqpHeRng5U+/NW1dSuQwNRYu5VkvZVO4E1ws9vqQu1lvXkZJJvlBcsOueBXoMisRkIpPbisXUNPubyaBiqAI+WJ9KFoDN/TmnhtFEcbOn3gw43Zrk/FdtdX+tW04tnWKKIAllJBwxOOO5rpIEvPN8xroMxAX7gGAOg4xWqFEkYDMWI6k0ldD0ZROj2N7MtzLCd5HBQkHHvzVi+lClI1GAOB/X+lRzX0Ns4jhJaQ8YHX/631quWMrlnJBPYdBVIlkqTupGGIwcjBxzUjTO7FnLFj1JOTUQjWlKj1b86tIlmKTsUEeuKthNighj070UVBRctWLRZJyac5JJ9qKKEARuflPqfSo9TuZILRmjIByB09aKKAKUEapMqjkvgsx5PetKHDxudoHsBRRQgYZCxn5QT6ntUBc0UVoiGf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the road?')=<b><span style='color: green;'>gray</span></b></div><hr><div><b><span style='color: blue;'>ANSWER2</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 == 'yes' and ANSWER1 == 'black' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if True == 'yes' and 'gray' == 'black' else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER2</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no
