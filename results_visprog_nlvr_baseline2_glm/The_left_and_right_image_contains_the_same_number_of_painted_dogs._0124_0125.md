Question: The left and right image contains the same number of painted dogs.

Reference Answer: False

Left image URL: https://i.pinimg.com/originals/9a/8b/dc/9a8bdc8b365236417576ae8dee29ae6d.jpg

Right image URL: https://i.pinimg.com/originals/da/30/62/da3062d3a59b288f8353b4ec186e6bdc.jpg

Original program:

```
Statement: The left and right image contains the same number of painted dogs.
Program:
ANSWER0=VQA(image=LEFT,question='How many painted dogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many painted dogs are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAArAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1Fb2W027xlCMqeuR7HuKTT/FVlqkTtaSGZUbaxjQnB64Ncf4Lnnkubu0eRmthavKsZOVDArggdjyelRaf8M9Vh2zwa4sQc+YAsbj37H3pShyux0VIckrM7ebVomOwRylsZwImPHT0rMuL9MElJQB6xMP6VV8OaReaBfXEE16L5rhA4dWPyhT7k9c/pWhcu1y9zBGoaSJTvUN93jPNKxk0zJlvVz92T/v23+FQrctNv8tJG2Y3YQ8Z6fyNaMsEv2Z5zA3lK21mB6H+dcVqmmza7qVw9rftZrERbvGckuRzng9Oe9ArG/JqEcFxBBO5iknbZErgjefQfnVXX9UGlG3ykUm8MTvYjpjpisOx8IXNnqtrezamJxDKrbSrZPPqTXR6XpFr441zXLHUZZbZNHmSGE27AFw4JJbcD6DpUzTlGyKg1GV2Hg6BfFst3JK62scSKybF3ZyWByW+ldafBoRGMeoISBnBh/waqHgjQo9C8Qa7pKytPbRJD5RkwWKtluce5Nds9rbpG7KuPlPIYilTV46lVHaWnkca2hXcVtFMssDB0DYKMMZGfWjTkk/tRIJVj3Knm5RiehA7j3rbmu4otPhQnGI16n2FYbarpek6sLu/u47eKSAoHfPJ3A44H1qZO0rI2UF7O7Wp2e7IziL8RRXHf8J/pYJ2wXbpn5XULhx2I56GirscpS8C6LGyXOoCSVHUPCY9wZWUgd8ZBzzXV3bkxQwrlEjVdw9Tj2qlpK2miWU1vai5mEhLtLMAMkKBx+AFWjG99FHPCC4dRld20qcCrpt2Sk9SuZt3kc/PaPeazFAZDCBBv3RkESfMSeewNFxp8NlayfZjLE7KPMHmEl8DHJ74FDrdWviF4nESLFbF1G4IFBboSffgVhaj4mfzjbmxnDsdueq/mOKpyS6lSlJaLY0zM4Uh3ck9cng+/pXKRTq2o6pGmWYXbklyAB06e1Pj8TFoS91aNAR23hs/QVn6TMb/AFHVZIQXR5i2XXoMnjHpRZCjvqdFbXBchGOQCu0+vNcm8do/ivxQ1xFvY30MancRgMMHpXTwRyRuGk9QAB9RXFzeZcfEDVrOMEmfU4FwBn0/pmsaqvBjhJKdz0zwA8NqtzDbLtRIwOTk8ux5NdlJeM0TLu7GvK/Amrx2jXn2jj5ghU+xauk07VItVubq2eUrCHwWEuw4zxg5z27VjTbSsjrai3di6vNNDHHJJGWt/lDHPA9Pp2rjvF139vitclVQyKigkDHY5J4rV1DX5BJcRBQQcoI8HBH8sVxq6k9xq2mjkeZeoj5XgglumfYCpe9wvfQ0LC01r7GjR2LTwMS0LhgQUzxiiqXjm8kGtQBPs6AWyjEicn5m547UVtGrJq6Od0Fc9n1HU7NY2E0qwwqo+c/livHNS0SRds2iXt3MDKVdJpQgAxkMp3evGDW7qUskzkSOWHmdD9KtaKq/aug+VSw9iMYNcNXFuErWOdy10IfDGklIZxrfnqWwUKyMx6YOCp4/Godb0DS4ZreSyutQZlfc4nu3AwPYmvSIp5GgRmbJIGfyrjfF8jvdIGbO3OP0rm9vefN+op7XODHhyNG3CSfj1u8/1rO1rSNTmuIfseSiJtP+kAc5+tdLJwD9KjxyP93NdEMQ4u/6mak0czoWmataa9ZT3RxAkylybgEAfTNaKJeyfEXU7myMRaLUIzl3AGCB+fGa0sDKjHauD8dosE9jJEPLd1csy8FsEYzXTSxLqPkaLjLU9L8L2E2i217LqelWt7G8oKvLMQE7hsL2OR1roT4psLOEuNL0SBV/i2OxH418yi4nAIE0gB6/OeaRppWGGlcj3Y1v7J9zp9sux9RDxqIh5TNpqMo2nFqSf51z3iHVbPXNT0sSakscttOrwxwWgUM5JHNfPvmy5z5j/wDfRo82TIPmPkdDuNHsn1Yvax6I+ktb+Gr6xdxT3Sap5qRCM+UibTgk+h9aK+c/t12Ol1P/AN/D/jRVqFlZEOo27s//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

