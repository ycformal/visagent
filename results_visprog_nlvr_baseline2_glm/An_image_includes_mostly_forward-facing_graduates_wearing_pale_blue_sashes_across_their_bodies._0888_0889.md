Question: An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.

Reference Answer: True

Left image URL: https://www.odt.co.nz/sites/default/files/story/2016/04/university_of_otago_graduands_take_part_in_an_acad_4eedf21342.JPG

Right image URL: https://www.odt.co.nz/sites/default/files/story/2016/04/georgie_austin_ellas_23_centre_was_one_of_the_hund_4fb8e31278.JPG

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAdAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzhtMup00zThbKJxatPlpNvmAsT34BxitGPSdSNpZ3SzfbQyH9wjAvAoyCXBwBgj16Grsd3a395dW+5FVYXO/qjJkYTOcnnJP6VXEU93LDbQ31xE2oKzTFxn7SQ+B8o7fLz67anTqW00aQ0qS5vm+0myjTyYt8rIZtxI3Y+TPORj8PeqEh8stF/o9qjEoiwsceZnoPTjHPvT5kvtPJe98qdkj3RRxoV8zr8xX2xjis6+g/s/R0vLe+lm80pNOoUKqOc4wOc5OPQj05p819wsakjWgkaKR1uJlUKYnQfvCBgc/72Opz3pbmGyeKBl8hmMhVm67Gz1JIAwWP6fhVC5t7ma3j1NlhgVkSUW8B3bgH+Y5Gdo796tX4tbmyW9SSzlUXfkF41+ZTnCq+3kA4JBHWl6Dst2dh4e1+8MC2NlovnzxlpmkafbGgY5wXI55PQA0kut+I9KN1LcWY+2y7ZIh5K/Z7NScfPISC+e+BxXOW2t6xdakujWN2UR7cw4tIjln6llUenT0q3qlgdJ1+Ialrt9Lb3IxJbzMGklaNMndx93dgBRWcaMYSckrsJT57R2X9f0yLVbu1tbp7i+uJNSvrS3yQ0e2K3Z+V2KBnrg5Oe1VRrdzdeHEilvrS++yQbxYQWYVZZGGGLt/GVz/D6etZVjqaajYXc+u2r3N1aA/Z7jLIG3P8oZgQDghse2R2q3a65eXXhWW7OmIdNsrzek4IQxyMxbCjo2FHIHQGjllfQLxtqbviDXLTVvDfhWeW/itS8k0VzI8JPlMAp+4DnB7V0Wo3sMXh+0lHm3M6XSFQkZ3E544HOMH0zXn+iaxbap8SbPULm9gVbpG5miUC3YLgBjjnkDnuDWjquj3s2p32lKGhuLNVuCI4yiXOCWDI6nq4JGR6DilOCteS0GouXwvuddq+rWn9pS+frsNvNxviMIyh9Dwf1NFeR6/qtrf6vLc2kE6BwDJ55AYvjnIAGPT8KKf1eX8prBYblXNJ3Ni1aLw3eX39paY+oQ28W1URtseGfHmMeSvfBIzTfCup/b/Hmi72mmK3QkCmRmCcHEeD6dzU2sak+iQrZRh5ZmtopWmd/lYNyUKYwV55zkk85qp4Lvhd/E6G/aFU3ySz+WhwAdp4HtzWse5zyd2anj7W2vfGGqQb1ht4VithIRkQ4wWIA55J5xzxWLCY9S0uTSpLyGQW8RuIruIMFTLAGOQEDIJIIbBIJHbpQvrh77/hIbuXHmSShz9TLWXb3UlussSBfLuNiSgjkqGDYB7cim0JPod3JJpcfhuyS1leU3MTQ3EWNpJUZZFPY/xDqMgA/erirjVrxJp/s944h4RSoAyoGFz+H9a7/wCJ9rDpenaOLGNbdUmZ0WMABCVB4H4VhaLo0d9pUETyACbErnZ1w2cf59anYd7lpPE1z4VfWL2zxBqNwI7e2bAJjBUFnA9emPc1J4AsH8Qa9ZaprF2rWOkK0jb3y7EEuMn0zk59q4XxJI6+Ir5SwOJT2qvb6zfWtlcWlvL5cNxgTBRy4HQE9ce1axklqzKcbqyO28Xaze6np0Okw2UkAtVl1C8jPUM7nDEegVgcdtxrQbxbo1/4X0XwobfEMduztcRjaI7kqwAx/EMEgn1bI6V52dcv/tM1wkoSSeHyJSo++mADn645NUhO69MVN7qxSik0za0fU5rQ26QtFuafcd8KuUOAMqSDjvXY2Hiae90+5Es+L6ysriNHQbSq71ZOnHHzV5nHO8ciuuMqcipl1G5SWeSOTYZ1KSBejKeorOpDng49/wDM6adVQSvun+ljt9HhstYtHvtUe5e7kkJd0jQ7uBzyRzRXM6d4pv8ATLQW8EdqyAk5khDHn3oq7voYep//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image includes mostly forward-facing graduates wearing pale blue sashes across their bodies.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

