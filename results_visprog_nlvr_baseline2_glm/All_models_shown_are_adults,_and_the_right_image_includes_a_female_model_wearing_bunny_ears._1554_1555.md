Question: All models shown are adults, and the right image includes a female model wearing bunny ears.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/be/19/ba/be19ba612f01ea7e74da83e3df0f5adc--comfy-pajamas-pjs.jpg

Right image URL: https://i.pinimg.com/736x/f4/07/cd/f407cdae56232ba6104da7c4552a74b9--womens-pajamas-pjs.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All models shown are adults, and the right image includes a female model wearing bunny ears.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABFAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1eSbaKo3F0wBwakmbAJJwKz7h1ChtwIPIwc1EpWBRuea+MNQW78W2kV83nWkQIiti3ys+OWI6ZJ4GfSvRPDU8JtCttHFb7HXzLcdYwR3PQ88jHY15j4n8Oi4iuRHvNzJ+9WYNyjK3APsd2PwFbngOe6sbaW11KRpd6hVnHJyvK89z2/CuH2l3d7npwpqVNwSPVpPmiP0qlaRzCG7EPDsy45xx3rHsPFP2rX30dbUu0SqZZt2AGPIXHrgZ69xXRmGOUZKA/hXbGSlsefOnKGkizp6S4lEoP8OCSKlOoWkTqrSgEkj6Umm26xedtUDOP6064tba6v0hmiVx5RkIJ77gBWdTmv7pUOW2peDJsD7htPQ54rA1/wAXWegxbHjee+dWaK1QHcwGMk8cLyOf51t3IEcDSIvzgADHGfavOtQmuo/H2rziFX+zWkEEJL7W5BfjtgnOT7VNSbirl0oKcrHOf8Lt1WHUClzo1n5AbmNWdXxn1Pf8K9c0jVLXXdIt9SsnLQTruGeoPcH3B4r5x8bWtwdba7nt/IeQBsZBIPvivS/ghqJl0nU9Oc/6mcSovoGGDj8QD+NEJ8yuOpT5D0to2J6mirJTJoq7Gdzj7uNLi3khkzskUqcehrFhtzalbN5PMaU/uWOQWb+7jPXHIx6GtaR6ijumtbhJ0A3L6j86cknqTCbirdDzXx5/a1notzfWcEqwxyoJJAu5QM9T7Z4pukWniG70TTriO70u1juIPtAIjZ3VcHbwTg9Dn0xXpXiS7sW8I6zc3AUQC0kMyEdeCPzPA+pFfMFj4g1Ww02Wygu3W3kXbgnmMZydp7Z/LmrpUINbXLliJqyTseo/Cm8u7vxrfG7ujcMwZ5HHIZwdoI9sDj2r3KJcivNfgl4bisfD/wDat5a7bi8JKM4IYRg4XA9Dyfxr1CNMCqkl7RtGcptwimWLVeH/AApVAbU3bbwsCru+rHj9BVW8F9/ZlyNNaFb0geUZh8oPvXPaB4pube6u7DxT5NnfwxrJuJCiRckcY4J+nWsZu0rBHY39X1C2t2iWQNIIn811X1A4z+PP4Vyev38GpyRXQt/s8x2x7uGLD5mAPbjn6ZpLy9kubphgEzPjPX+L/Aiqd5pUttYSkujRxbWQd14wc/mfypVl7rRVCb54tdzy3xXJJLq9wjdI0yfmzx1rrfgrIyeKbu33EZtN5Hrggf1rA8W2P2LWfLIw0lqpIJ5OP8eTWt8MX+y6xHqXnFdgMJTPBz2P6YrClokjrrtO7ue/8UUdf4aK67HEedLdszNuTC8Y+YVJbW89/LshhYrnlsjA+pq+LOKRwDGAvc10lrBDBbqkSBEA6CpjFvcT0OF1n4a2et20q6lqeo+W7BjBBNshAHT5ccnvk1W0P4c+EdNdGi0yGQxnJnuSZWOD78fpXW61qcjabNHpRgnuWG0b5ggHqc4PPp71iT3V7BNYpbWSm0B/0jM6b1GOABn5jnGfpWvPZWGo31OotFiLMFKgcFRjBGBjFSLIv+1/3yay4ZxIA8Z/PqK1reRZ4y38S9aPQlo434iTtHpVuyEBAWLvt+ZRx07/AJV5tolzJrnieysbq4uLmK1l81fPO5lCDOM9cZ4xXsviDRf7cihtldgvzbsHAwcdawZfDtr4UtbiWzLz3MyfMOFGB6Z6nNcnK3Vba0/A2UYRp817vsZei3Aub9z3DIORyDlgfp92tvUIZJLa58tPMWVG525wQOBisLwmipb3N3NG8UkknnujDovQEfXBrp7j/j3UxZAbBwOMg+1dD7HK9dVoeZ+KPC/iDU9RXVIolZHCEu8iqIxjGOewH862fh94XNvewSMCAZzJI/IyF6ADtmtuXXLfUrn+zo0aSxRMzXA6Fs48sep9fStNdWt9Lu1dxlWjwkajBznqfTjArOKUXc2necFB6/5o7sOp6GiuOXxMzjK2wA95P/rUVXtodyvZS7FWOGL7bNKZXDhxwHwBx6Vqxap5LIkj8McA+9ZEsUmQwigaRiAS2QP0zULRXNvGZL60gjXOAYZS+fzUUJTjqVa5ranpn9osLmwuWt7n+ID7rj+h96x7Nrvyvs1zMUuVlIYyKM7cZ/Kp7W7eKNZreGRVYZ2kj+VYl9c3l1rsDPblnkcJGE7KOfwwMnNTOd0rFU6V3Y6mOGSEBmn3D0CAZq5AsiQyMjBXYYXd0+pqMRrEgdtxReAAMk0v2mLJJ+0ew8vGP1rT4VbqZ7l/R0kjadZmiOQuNi4Peub8e3j6Xsu441lGwApuxjmtiK9hjLSK75XG7epGBXI/EDVYJLEyM25UVBgDryTXNUmrcjOihB83Muxe0+UTWdqXjEbXJDsq88dsn6fzqbUtTgtisLxu0rsAVj5CZ6Emsiz1WDVNFsby3I4iXK4+4yjBB9CDUOuSxS6HIUTbJ5Z5PeiVXksooVOj7Ryc2U4NeM+xmt0bcTt3fIR+X9RmotTeaW9S6DF0cbdqjOwD6etc9pAkkhaST/V5/h7H+ldLockYu2RDI7FeMjOPeuiUVKNmrHJGUoSdnf8AL7y1bXP7kZJ/EUVqxrcbAXdGJ5BHTHaisXhor7RqsU2r8rLTSs91b5/ikXNWdVlI0q/JGfKZMf8AfIoorofws1Ofa/lj08RuFcMm0lflPSs2Hak9p5A8o2+2OMg8qM9vzoorjm7I2oq8jvdMmnuLVWuHRnBYZRNowCccZPNWJLdmvI7nz5AI0ZfKB+Vs45I9Riiitk3Y5ZL3mZmqs9wxgVygwGbvuGeh9uKy7Xw7YxFEug92fvsZDwzE8sR3P1zgdKKK45u82ddNtQSRYutHtjC6Q5tweAYsDH9Koa7Cn/COxwsM5Hlsw4JHQnjpRRUvQ1p6vU4neNKtFsrbzPKdwf3j7iD064zXX6Q0Uemyxx28ahlAcjO5/qaKK6sPOTqRTZx4qnFUJSS1Fa6nRtquFUcAAYAooor1HCN9jwVOVtz/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All models shown are adults, and the right image includes a female model wearing bunny ears.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

