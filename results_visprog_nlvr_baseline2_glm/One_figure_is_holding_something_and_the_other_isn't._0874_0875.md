Question: One figure is holding something and the other isn't.

Reference Answer: True

Left image URL: http://facultyregalia.com/doctoralregalia_pics/doctoralregalia_jdgoldp.jpg

Right image URL: https://www.saxonuniform.com/regalia/images/Custom%20PhD%20%20Gown.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One figure is holding something and the other isn't.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABMAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDgqKKK5j2SJpiCwWKZto5KpwKsWbx6rLeC1hlhNrayXTq4LDYgGcHHXnvx716t8KoGufD2oRCcRIbrLERqTgIOMnqD+mPesPxPFZ+F7/Uryztw0mpwPYbCdu3dgtIABjovI96iVRfClqc75+bRnn8MqTxLJGcqwyDjFPooqzdeZaQYUeuKXbgdDmrUQi+UMMfKOakZBsPyjrxUKpqccqdyHT9F1vVZLmTT4Ea3twpd22gKT0HzEDt0qHSp5bi/u7DU4ghtbaWYPEgV18sE4I6NnPfn0PavQPh9BBJbalLcxK8FvJFI4ZsBvlcAEZ9a5bxjJ9k1JNRsAEkui1qzBQUKMOR9cd6uWKk37JJEKgrOVzGZlljWSNsrgFSO9H7socnBxT5TzgHimGPKk9iKUmmEU0U2VWbIop4YINu3NFK7CyG0oGWCjGT0ycUlZH2lnvH3dM4ArSMeY66tTkSPU/AWsDRdSm0fUb1bO0vEMiTFRtMgA/iPQYBH1xWh8Tbrw5a6RBbi/wDP1Fis0EUB3YDdWc9gV6d+leby6x9kMdncQJc23kxEo3BDFQcg+vNRWerwtqEUVpYxQKz/ADyt88hAGT8x6cCuj6vGym49O/8ATIum7qVvzHiOTyxIY3VD0LKRTaxZNQuJssZWJ69a14n8yFH/ALyg1hONi6dVTdkaUTquzdyBjIq2rCWVYo5F3P0DMB/Os9CNgqheME1CBwfv/IfwNZKnzMwc7HXWU0/hfX7S71XSLm504lhIsXIYYIBA6NjOcVa1/wAU3PiexFhoWgpDF/y3vLpRheeAmeE7cnnsOOvOXOs3unXSQ2t5LCscaAorZUnG45U8d/SqZ1LUNUuA95dSziNWkVWOFBAJ4UcDnHOK9f8As1+zjUaWivfXtfb/AIPyOB4l87ir7lhWhC+XJeW00yj5vIJI/PGPyJqGaTChVbIPcViRyFGmHORwT+VWNPmLxPGxzjkV5cqdtTqjO6sXwowPmoqIsvcZ/Gis7F6Eibd67/u55wccfWsO+iW31UojsVwHG7GRkdDjuK3YyVcMBnaCSCu4YxzkdxXO37QnVJGtxthU/KPQf4V00ysT0LWquf7Rb2SMf+OLUenNi7Lf3YpSP++DTNRYNcxt/eijP/joH9Kbp5zcSD/plJ/6Ca7n/Bt5foY31IoYZJbh0jUEqpbqAAPUk9BW5ZcWca71cqMEryP/AK9YlqXL3LB1SPbiQsu4FcjjHfnFbFgR5LAFzhur4B6eg6fSuGexrhtJGomNowT05qnrQZbW1chisbthyAM5PQew4688+9W0K8biAuOf8iqOrNHOkdnbFPkG7ZGrfePJBByc+pPpTpq0HLzMZv3rEV++7U7g9cHj8gKfYS+WZDj/AJYkY+rKKqyyCS7nbpz/APWqa2OIZ3xnbGo493H+FfQ1H/sra7HEl+8KsMYlhupnkCIrLnjcSWJwMfgaktUWOTKCZ8jGTHhf5mnWkLA3JV5FZBkLGfmf2H55/CkYOHDPEQQfvTz8/lxXgtXVjqj3LVFLxjpRXIbk6O0bB0IDDoSM1neHdCl1zxAujCaOK4lDku+QoCqTnjk8CtCql1fXGl3VpfWUphu4Zd8cijkY/mPatIt7I3rwTXM+h7H4j1HQbXwFdWMxk+2aZp5sdixAxPKYwAenOCOG4x+NeCWDYmmI5xA/8q3vEPj3xDqsDWEl1Hb2c0Sme3towiSlgGJYc89PyrnLN8G4b/pgw/UV3X/dfI4kknoOtSoO5mZeGICvs3H0z2rX0qQSQybQgUNgBBx09ep+prAb/VgcYrc0RNtiW/vuSPp0rkqbG2Gd5mzbyvG4YHBHQjtW78PLXSdX8XHSb9SkTwvsySgeXjCkjB9T7kVz8Peo5LZWLzK8iMp8wlWxkjofaik7+6ZVFZ3Lvj3TrvStd+zXukW+nXKQgO9o5MNzycSKD93jAI9RWPp2HtLsHrtT+ZP9KdqUsk80zTTSynC4aWQufug9SaXTwBZXh46KP0avdlh5UsJvo0vxZyqfNNsZZpDLGfOOFABJzjnZxz25xzUHC8A2kR9FXzG/r/OpLazuZbCW7SCRoFkCkqpxkDgE9Bwc/jVSOIyMUjILdz2FeO3obI0V5UHlsjrjGaKkDCJQg5CjFFcbOq6OL/tS+/5+5v8Avqo5b26mx5k8jY6ZaoKK6bI5nKT3ZI08rnLSMTgDk9hQJ5VDASMAwweeoqOiqu9iSZrudpPMMrbs5zUv9qX3/P3L/wB9VUopWGpNbM9As5f9EhLHLFFJJ7nFTysBp9wx6lSP0rOtHP2O3/3FH6VZuSRaFexBqaC94qo9CpfH58nvHGfzRams+NJu2PdgP/HW/wAaq3LEwwH1ijz/AN8irMJI0K495D/6CP8AGvosRK+EXpE5Yr3jr/Cfi6HQ/DExnvrZNsFxbwadCHMlxLKykyy/wgAKFX2Fcx5MUClYEAXue5rCboK1GkZhye1fNTjrc64voTEjviiqwNFTYq5//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One figure is holding something and the other isn't.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

