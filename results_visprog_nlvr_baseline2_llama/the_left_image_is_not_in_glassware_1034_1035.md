Question: the left image is not in glassware

Reference Answer: False

Left image URL: https://i2.wp.com/www.livewellbakeoften.com/wp-content/uploads/2016/06/No-Bake-Strawberry-and-Blueberry-Cheesecake-Trifle-10.jpg?resize=680%2C1020&ssl=1

Right image URL: https://lh3.googleusercontent.com/sGl9Vv-xax3Bz6GXj_NLvMmDI5xIsfzJ4MfLEYbnNbH6Rn_IdxAyoxHrd5wAgzsZkknUXt2uG8Q2w6pasp95bdiZIczjt44DFQIwiqhB=w600-l68

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the image in glassware?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the image in glassware?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigBKSlpKBjcUhFOpKQxKSlpKBiYopeKKQEoORkdKgN9aCcwG6hEw6x+YNw/CsTxBPcadY3EsFw8an5SNw4zx8vHB9K8zk0GwkUmO4m87JLSSfM2frxWVSrKLtFXO7CYKFaLlUlbtpc9a1TxFpGjJG+oX8MAk+5k5LfQCq1x4w0C3tYLmTVLfyZ22xsp3ZP0HI/GvIL7wwlxEUguAynqHLdQT06+tZGs6X/ZxtV+128U7oRL8zcR4wCAAec/SonXktvxOill9JpuTbt26+it9+vyPZtd+IegaFZw3L3DXYlJCra4cgep54FS6T4+8OazaC4h1GKHnaY7hgjA+mDXgsVva3CtEL6MnaQrNI2eB/u1HHBaXQMb6lCrsNpdQx2jOe6devNTHEc17u1jWplkYKKUW79b2/4H4n09FPFOgeKRZFIyGU5B/KnbhXhOleFb13ilsfEMluAgO+NHzz6cgY4/nXqXhuO+ihksLzULm/xGG8+SML1425HX860jVcnaxw18JGnG6lr2as/wDI6TAopQMDFFbHEVboRvKVkVGUc4YZFVDpWntIZWsoGc8klOtU/EGoQ6dqVlJcRyGF3ZHcAlUyMAn2qHT9bsH1eTS4btJflLRBecEfeXPf2+hoa12HGTS0ZeutL0+45ks4s/3lG0/pWLqum6FboZ7uytCEA+eVAx46AVq6lqUNi8ayTRgucBS3zE9uK838aahIJlmupBCojLDd91V5zXJi6vsoXSuzswkJVZW5rI7q1h0y+tY3SztJoGX5P3K4x6dOKh/4QfwreLxpNvGVPLQEoc+nBrkvCMGoWDeZP5kVnNHlQQcMeCCT0HGeK7e2u5URY7SHzTIR824AAZ5OfpUxn7qc1qDc4zapydu9zQ0vw9Zadp4s1BkiBypcAMvsCK1YoordVVBgdBk561T/ALUs4nlhe4UPGfm74NSRv9ovo3WUMgjLBR78ZrohKN7I56jqS96d9S7iilorYxM3UsGYR4BD8MD/AHaz/wCyNOzK0dpFHLKDmRFAYZ4yD2pvjKW6srSG/tQcwt8/ykjb745x71X0fxJYalCDuVJO4JBH5j+uKHvoLoU7zwfZSwIIpZI5gMNK3zF+O/5fzrzPxV8PfEur6gNksYtViEZBuM7jng4PtXtHno1yYlIbC7s561RvJghdguWA4H94+1EpO2o476HnF43j3Tbi20yAm5QwbYp7W3DIGUcbt3Q5GDn1zUelWvxAstZsIp1uQkqthPlZR6lscZBOefavT1lSMF2J2r1wM5qpo9/c3uqG6liKxoGjVM42IT39+K5qlVRtHqzop027y6IxdK0HxIdevrfUEU27IGW7J+TeCD93q2ec9q9CsrWO1QohyQMD2XsPpWY+u2NoZWu7hYQACqt949uB3PtWV4b8V215d3cNySlw0hkJ6pGucIhPqAPzJqockLLYbhVrXa1sdjRTBLGRkSp/31RW/MjmszlpbpiWBuJMHIIJzmsm48E6LfRie3kmspyMl4W4z/un+mKsucg5GapSNdCcGCV4jnOeqtXTKKkccajjruVz4Q161BWz1+ORewlRlYfjzVJtG8aCMyx39sV4I/eDI9+RXX22ovcLJI8flxQx/OxPVj2Ht3/KsvUbl30qUvciGNivzKdrDnoDWEonXG2jMJrDxvJbusmo26qFyTlfX/d5qSDwxrty+3UPE08anqInbn8RitrQbKeaxmSKSaaNzkPI5bJx2P1FW7bwtq017DLd3caWqD5oASWZvXIrFxZsnHXU4nxvp8fhzR4xaSXVxdzMFN1IwKxr6euTg8156utz6Xo0ptLmWK5bG7aeGIbPzA19H3PhfT7uDy7wfaVzkRyYK+o4x2rN1L4e+GdTiRb3TgQnTyj5Zx6HbjIrKpQlKXMmd2Ex0KMJQkr3PEmvBfu15LJM0k5MjHzm6nnA56UV7XB4E8H20Kwx+H7RkQYBcFifqScmiuV4C7vzHpxzmgkl7N/eRzXCICWCgeprPidpZhKw27m2InoD3qdvKdGBJk4PIAxjnrTTBGsZUJj1PqfWvcPjSxeAT2SW0RAizl+eWp66FaxtarqNusts7BsN91WHTI79aqWm9ryFJDvRnUZbg4zXR+K0Y6C3lffUiQY9qyqaI6sMlOaT66GxbqirhAAi8KAMAVj3F/JLctHGSFzgAd6mstRDWUM2RiRAce9NsLbfM8pXgHispXdrGqXK3zdC3bL5G3PJ7mrbjcQR0PeoARu9farMakDJ49qpaENibPp+VFDXEKsQZFyPeigRxP2ZIgcZYEAYbnj0pCd0xBooroRxsasaiaM8/KwI5966jU0E2k3O7qqNjFFFRU2N6G5yvh/TTLYedLf3jqhO2LzAEH4AA/rW/pp8gSwx8Ix3Hkkk/U0UVzQO6v8AEzaiVQiHHWi6yY9uSAeuKKK1OUrRACNcAAe1FFFMZ//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the image in glassware?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

