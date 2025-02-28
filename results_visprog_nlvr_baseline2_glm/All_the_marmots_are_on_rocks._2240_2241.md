Question: All the marmots are on rocks.

Reference Answer: False

Left image URL: http://dwarffortresswiki.org/images/thumb/e/ee/Groundhog-Standing2.jpg/300px-Groundhog-Standing2.jpg

Right image URL: https://bluesboots.files.wordpress.com/2017/09/p1050622.jpg?w=311&h=233

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All the marmots are on rocks.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAmAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCBFVWY+WSAKlkMMKKznah6biF/LNNRlfLDgDgDpms3xBfyWVnEY1Hmkna+c7RjGR+dfO0qPtKig3oZwjzSsbEEcEyKyMrKeBznp9KnWKFRhnK+w5rG8OXbtYyW0hL3EZ3FuhdW5yfft+FbKvEyFlPPQDA5rKtT9nNxTCcXCVmPKwqDgk8YwRgZqlNbxZUhcY9DxVgh0APDDJG0kZOKg3ndtIODz2NZfFGzEmcZdRTrq86+UmwucfvAN3Jq3Z6Vfu6NJB5dsXCkPjcFJwceuDz9KmvTGsl1ISRH8xIVQDuB6ZPeoYdZV4pGS5URmMDDv0Yn19f1r1ItpbGznbRGlNoPycShp/lAIBGQOWbHuMcVWbSJrK0jmnCyN5hGMEggA4IzgjPP6V1GzRdBjtzrOpzCeRd6xwxDAGByGPv7VNcT6RKiyWF8twkpEY86QZck8Yxxn/Cr9jUau0Cuzl7KLzH8pohE8SlzK7DqB3GcDnHPYYq5I85hiM2As8e1sYGORkY9TWtqmhfZpiksjuZY9uMfcx3Y457c1SuLN1UR3NntWNfkkUbl9jnHIPf3rJ6BKMoq7OWbUBaTzx+ciL5jFd7MCR2OB0oq5q+iWZ1S4LdS5OA4wvsMjpRV3j1ZldmmkqInyou0N/CM4rn/ABW7TR28cZkVVBbOMHqK6F7YvHvVCvt3/wA8Uj2yzEiWLcoyCfw/rWFCSp1OZihLllcyvDk0U90853eakSxsc46E5rpWxhPmHrggd+9UraGLTVb7PG0YZGR1HGQ2AR+gp8i5ClQT8uQRycY7VniJOrUcrFTkpu5ddlaMEtt9lHPSqu9twbvjj/PpUflOuMuc7Nx2uMevamSLK+4qWOVHb+VZLVEHG39nI2tzvcPI0TPuXKnaAxIHp3z09KoX1lHBcafbQuJHDfPEpJZ37EjtjoO9XNZ8Q6hJdy2sUphSM+T8qgEhT69Rz6V0Hg+60XT5o8NHNeScP5oyT7D2P+FfQ0cPJRUm/kWnqQanpl54hs9Mim1G3WROAoGSisM8nnJ6Z6Cpv+FY+IoobW50q9ScoRKAZAh3DkEDv3FenNYaK9xDqMlsRcRpw0JK9T3A681e0zVIHgKxzQ4OT8xAwM9MdvStmrIvdnE6HD4o1YhvEFq0ESYB3sQ5A4xt9/WuzhlksrM/u4nhQEAAkEjt9Kdc6tBnypJY1dzgYYZJ9AfWs65hIlRQrDI5xwRWahFO5pzNqxkak1g19Iz6fE7nliwJOfworZgglkiBAjfBwfMC5X26UUezh2Fdny59suR/y8Tf99mhb26Q5W5mB9RIaKKuyID7bdZJ+0zc8/6w0fbLn/n4m/77NFFFkAn2u5/5+Jf++zR9suT/AMvEv/fZooosgNWEtJCrE5O0EkmnLI0bHaSp7kUUVu9iFubNn4y16wRI4tQkaNDwsnz/AIZPOK2NH8dXkdw5u7aKVJQEG0kYPJzgnHTj8qKKyky0blz4ijvdMF5b2ipD50jyQSHIYhSMgjoflrfh11orTTVfe8VyiEBuSoIHfPvRRUMa3J9XNnFdrvslkdowxYuw9fQ0UUUky7H/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All the marmots are on rocks.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

