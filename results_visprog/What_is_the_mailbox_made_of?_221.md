Question: What is the mailbox made of?

Reference Answer: The mailbox is made of brick.

Image path: ./sampled_GQA/221.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='mailbox')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the mailbox made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='mailbox')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCACWASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3jg9RTDijdRnNWQGaXPvRtB9qULihgKKMUdKXOaQBtNOGRSA4pd1IB2aWm7xTgRSKCkxS0UAFFFBoAWkpKKBXFoppOKN1ADqKSjNA7i0tJmigdxaKSigLi0UUUAFJ+FLRQAhGKT8KdRQKxERzkU8ZxzSkZHvQBQJKzCiiigoKKKQ0CDNLSZpu6gRVDe9Ln3rl9L8Y2d4/lXYW0mJO0FtykfX1rpA2RkEYPQ1tYy5ibNLuqHmlzRYfMTbqXOah3UoY+9JoakS5x1pN3NN3UuaVh3HZHrTg30qOjIosFyQn3o3e9RHjqaTNHKHMV7vVGtLmGNotsbuFM7thBnt9a0Q3FYXiOya+0aZUOGQF+E3E8dB3B+lYfh7xXAbMWjRTIyRF0d23A/j6Z7moegcx3O4UmK5jwnd6hOLgXbOYR80Rl5Y5PUHuvBxXTbgeKQ73FGKXikFGBQAuaM0mMUUALmkzSUfhQO47PvS0yjNAXH5pQc0zdSg0BcfRSCloKCiiigAoooNACUUUhoFcXOKaTzSE0wk07CY7IpdwplFFhHhk0qTkEIowPmaPgDB5yPfivQPC+vNqjG18qKJIYV2gMdxxgdPT/GuJWCKO3ORHjarGQgqU4+6AeOc9+tafgx2tdUlLypHEqMzF8Y9+c8duTWxij0oORTg+R0qFZFfJVgR6g55qlqOs2WlQPJdTqpVdwQEbm7DA781QXNQMDjOacNvrWFo3iXT9cLLZtL5iIHdHQgqCcfStgMRSsNOxNt/2qXpUIc46U7caXKF0SbhmlwPWogaX8aVh3K+qXsem6bPeSfdiXI4Jyew496zvDuttq1oDLG6TqMnK7Q3JHH0xith0EiFGztYYNeba5byeH7+DULFj5ETGQRrKXUYOM5P6jPfp1pPQXU6/U9WPnTackr2kxj3RzbAxYd9gPGevWvLrx47e7dLK7aSa23Ru0gUq+CcBQM5BBwR05q7d67BqaNc30UpvHTajK2ACOhAweBzx0Nc8A7XLmNsRTEM4Bx078jjHtWUprYDpLDxJf2KC0spJFaTBMYJcg7cEKO3+6OmPauu8DXGqSSXAvJd9uYw675CxUk4HHbODke3vXm0Fxe2l/HdNEoMTMEPG8t0Ix1H3unfjrzXT+HIJLmO1X7YkVsrbXZGMRdcnkhu46YPHQVVurGj1hXVuARkdRnpTqw9B04WUbyJem5SUnk84weBn885/StvNBoLnmkJoBzQRQAZpM0DBFDHjFACE0tAUntT1BHagBBThTqSpGGaM0nekIoC44mgdetNoBoAfSE0hYY600sKA5hSwJ60YFNBB6CkJNOwrik0zNKaTNUkAfjRzRmkz7GhIls8FnaY24+yXUs6Im6XzPlCem3PUf55rX8Jae+olhwwUhyJOmM9/UVj28mpz5VbiNWjUHBIYMDwAMjqPT3rb2vBpgSztwgJEc5jQxOcr065PTP8AStdDPqdautWegyHTp4p1xl/NwSrZwS2e3/1qyfFVhb30a6hZqLqSUqQBKAFJXgseoGMYArmft73LtbXY+dm+cy5DKoXGBjnketUvPs3vUWznksbZcHzERnHA+8R/e6YxSuibGnZpLBdG7sI5YUtWiaWK5kKlu+SeDjPtgcV6vavLJaxPcKizMoLiM5UE9ga8ls7e1bXbeafUrTUYribYWuInXc3o2eg6fjjtXrqIEUKoCqBhQOMCmh20JBx3pwB7UwA45xSjNMB/PWnD8KaCRxmndKTKMTxJqGo2FkWsYuwzcMAVTJI6Z69686128jvLG0toJnnt1VpZt6HKyk88dBgHjBrf8Z65cyvNBFAs1raTjdHhj5pUfNuI4CDI/EVyZ/1TAHzAxMkSID8x+6BjqOpyefu1lJsDn7q4fznCnanCqM/Kv4fgKsI6FAhfcxbGVPzfQf40kulsY3udp8mEDPz8EkHA/QnHtWSUkChjIFVWB3Drn+lZ25kMvNI0V3K251EcnyBmwPY/XnrXS2V/aW8SjUbdJ4lVx/rMHLDG7+Vc3Z2yTRyRtdRxkKHzy4fn7vH4nNSNctayhXkDHkDgjj36VEm73Gkex+CIs2YlW/LkDElqMAIexPueue+c114714j4c1C/u9TtI9PZIps7FAYjjqc4z7k17NPdJbJvmkCKeMk8ZrSOqKLNL1NZlvOZNzpKznJz6ccVfDGrsK5Lj2pQKi3Gjd6mlYaZNxSZFRE465o3DOM8+lFg5iXdSbqjzRkUWFzXH7uaN3NMyKM+lOwXHEk0nNIWIqk+r2atOgnQvCjO4zgYHXnpSEW3kWNGd2CqoySeABTY5UmTfE6up7qc15RrPjW4uZGEUrE44hIGzBPRh3+U9evtWbpviC5g1qMzXMsULzKLiQ9Np7Y78CqFc9tHtUNzdQWdvJPcyrFDGu53Y4AHrWCfHOkNpN5eWsoZrZciOQ7S/OBjrmvL9RvdZ13V2uJnnaNtwSN/lAjzkAgdP1qHJLVjbstD2ez1bT9QJFnewTkDJCOCccc49ORVyvGY0g0yeO4svtMMy4JHmAlTjkZA5H1r0bwzr6alCltcS77wZ4Cn7o7k9M1MasW7ISd9DfoqTYKXataXK5WfOdsYFu0YviA43KASVB4OB3PtW9LrcP2jyXiFzp0XEMTsVYn+9nPX+WMVxwZNxwwxnbu74qS0vGicMYxNGMghwcDPfimrozbNbXtc/tC6l1C1hS381CDG5DEDgZ46H/IqIS6fd+WJbc6eUgYSPG3mrI3G3jt3zWdevGZ4/lUkRBWRFwo57j1xzmqU6Ri5iihHk5ADb2LAc9TVXEdVo0dveJPZHXFtpCwZEuVAWXIxgnB/POK9E0K9j0jT7qLUtWS7u4CWdEl3kIBwFzgZAz0rzLR5ljuoFvI0WMqPMMABVh/dP904/wA81av/ACnuWg8tYg0jNgRlWXk44PQYPA9qzc7FI9W0rxNpWrzGG2nKzDpHIu0nPp69K2sj0rxWwuzDqCXFi7xxxsPLljUg7uhAHvmu1s/HK2WkyNq6s17HIybVXbvwR+XXH4VSn3Cx0usazb6PbCWYElshVHqB/wDqrk7j4iT7oIoNLYSSQ+a+9s4XBIIA7d+aw9c8dNrNu1s9okKFgU+bnr39e1Z1haT67fwxxpbqzE58plDEZAIOe+Ce30FHNfYC8PHd7NYyWwZJYpwTJMqFJUJxnaBw3J7duuKzn1TSbe7e3GpGe33kIWUkxoAMlQBnceVHI6E1q+INsN+0FgkCmFmhX7O/O4NnkHoQO/15rnJ4gtrJHc28ZLkvhGUHcDjcT34PT3qXK2gzKvL2KJpY4ZWubbJVN+V+Y9cDPTmkmMfBu7ZGZZgZQrbWYDqDjgZxjNMjmGmSywpb27gnf++G/AwQOfx6d6qu80mm+cwkaIHbG+VBBzk9eSOf1pXS1Bamotx9mlDR2yNbqCCyEZAIyB/9aoQY5QSsbGUJ0xuBHUfp3qjbytFCbcKGWTD7wf4cc/h059q0LDTbmYM8NpPOUPOxQAfVfeodrj3O9+GMtzd6jIzwxC3giDhnj+YEDaNpH15rrNd1uCRrix2TP8mAFXOSOcYPQ4/GvOvC0GraQl0oS4tluUBJTO9VU8DPrUPiG71vUE3zW91KxGN+zBwDkcDqeapNbDszSbXrl7SMStciUAEh3I4zwCB0GP171v6Z49ubPTZjqKedIo/dY4wfRvWuEgs7+e2ijEdwZSArK2VGPckcdP1q4ND1AoQ8OWzkFXXIP1qLvcLM9Gt/HtrOu51aMxxbpEwME47H36Ada5fVfHt/JMLu1uvKhJ+S3XA2kdmPft7HkVkLpN7GQr2TzIwwyFxzx9fxqlL4fvQSI7WQMejKwZRx0+lWpdwszuLL4mebp0vnWqC9VRtVT8jepz198VRj8UG8nju5ppBcLkqiPg9uFOORntXBvZ3lkitdQSRg8KWTjP1q5CqqBIrtxzzxg+metDlZk7bnuejX39p6ZFck5Y5DADGCPatDbXmXw+1m104zW17MYHlO5Sz/ALs//XrU8R+OPLj+zaU+JC2GuH4UL/s9fzIp3KVjudpqnFqdjLcTW8d3E0sBxIm7BU+leRN4jvpEVku3RjIJCI3IUNjk47E+nSs6a/cXALByhwdxbdzSc7CZ6Tf/ABC0yGcRQq0yFGLSdNp5AGPevO9T8Sm7aOaFnhWNMFCTt9xjpg9xXPzMzlmLhV3csRwfWmJNttpA0qsWGQhUkD8PWmm9ybli6uEulAhVYpUzIJQx6nGBjp69Kis71ULo5Jkl4LMx+X2x3rGaXY0p+ducHa2B/wDrq/Z2E8qrdcMmQMDnB96uTUVdk3Oqtrdbe2R5Wy/GVReMetJJqDoyIGHPYjqRWbcXvloF+XHQFue1PRlktVAyZPvAg5x/9avPlFyd5DLGoXM2Q6jG7jd3zW14Y8QS6ZJJMsIlbG3dnt7etYkM5mBLkMewIxik3OJlKRnYVyD7+woT5QPWdL8QSXcM0ksscaqNyGTge/vRaeJNRurcSxadDKuSNyTcEivMvOuAnLnYwPHpimq4my5z1/vVtGv3HzM4kPsDYwSOMjik+1StjceM4AxgGn/Zitu0iM3HVmXAWoELIMyRZ+XILZ/Suu66Ej43Csys4JPO7PvUYP75tzNk54BqCQyNMXI685GMYqSO5WIg5I6fMKTYzUtYJ5Id63pHTchODtq/JdPKMtullxhWzndj1JrNE+9Q8ihEb+L8Kmspg6tGrncfUABV9ev6VhK+40XWLQhWzIsedzIjcKx4yKgmvJ28u3Yo4HAGfX1pXBmLxqdyAZAHGT1/yaqTQfK0kvESjdvUc5z1/GlGXRgRiUNNIJjnYThc8A+tdFoPiSXw7d+aqxvlSCFTIbv+HPf3rnt0ZUzRg+aQDh8DcPUVPGrzGKQQNIzAAKvO4jpwOattoaOjk8S30Gw28UaAqQ6qqlCCckMP4hnPX8q52W9W4dX8vkKZMlwBg57Y45/lXTaFoF2ZxdapFAUZSJLdlzvGMDODxitF/CulOGCwPFuIb922CTzz+vNCd9WVyM4G6V4JBFHPbyhlU/ISc5HQH26fUVt6LpF1cwPLEI08uRVxngHv/wDr554roLbwhpFvMJTHJMR0E0m4L+Hf8a2woVcY9hj0/pSKUO5h2/hi0Fz9svMz3GOR0TJ6nA69T1reQeWoRFVVXoAMAUAgcgc9KAPTHFBdrDgTkZBpdzdgc47UgwG9TSbscd/Y0DH4wPn/AJ0u49fzFU7rUIrOMtM43YyFHX/P1rlNV8RyT7kVxFAASSOQfr6n9PanYTdjsluFe4aLd8wA6dBUoXHIwfeuC0jXZrfUY4iTIg4bOAcY6Cu5hu4bqINC4bA5HcexoSFF3HyIrDawBB7EZFYF94YSVy9nJ5TdTGxJX/61b2c45596XAP1zQNpPc5tTHp8BhmjljllUpIY16D1Bbgk9MCudnukS4ILOo5BJ65z3x/+qu9vHtTEyXKrIp6qf88Vzb29jbO0wi2hjkb23H8BT6Eez7GVaQXlwx3gJGOhZMD8PX60t1E9vEZI1R4hlt6c4PHFW5bl7s7FYohz35OPWoEd7VsL8w6EYzkVLfUv2PTqY6XkhmUCaPaT9zPH15/zzVKeUxXDEMC3VdvQf/XrYv8ARor0NLY7Y585aFujfT0PtXMSLLBOySo6upIZT1rSNnqYSg09Ql855CGB3seOOtdLpjS2mmLC8cizN8xRhwR6+n9a515iLsSxvjkFOM46V1U0yy2ib41BwCAPX6fjWWIbaSJK8oRskIr4H3tx/p7VXguBGwwuTzlQe2KV7iQQvj5Ext4/w/CqqOqybtvzHv6VnGOgGpDOUfGxQrcAMw4BqwJvIDbcn15IH1xWXDdPI3mHJYEn5V/OprmYvGDjceQcDH0pOOozVSaSXBVg/H8a8/TNNuJVhdUfaSFFVIHeK164kVfTrV6CYtEPlQ44yRWbWugkZUkFpGhhX5nmUrIRkbucgjPbtVa5Q7iGhjfyxt/dDLMQOx9qR9okjmMrFCAilgPlPv7da0YrtgsiwyyMz4CjHyoO3Heq53HUdzm3UgyCK3k24xyckZ/p/jUdrLLC5KKzA9V7H61LeIZLxo/NQSgkMFyA56561FaB3YBRyPX0rrvdCNKV7eTTQfK8vB+Vd23HvjvVaImGJCMFnPy5OMCi7V5pSyoxjXgLtwKhiySJWCBUBVQTja1Z9ANCW/jhZRFKPL43gc8+3+FORpr6OWN0LxBT9wdSO4rKdVYR7xsEh5w3B9vatK21OGCNkRxkfKAcgFT1ANRayugNfRvBtzcxrJezeVAW3LEhy7D3PSu1sdOtNPh220CoT1bqW+prJ0rX9KGmwRG6hgKLt2O2CMe1aA1zTWHF/b/9/BitLt7nRFJI0Dnn2/GlHXk89ap/2vp7EYvrYj/rqKVNVsJgrLeQYIyMuBQUXOQdvbvSc4+99QPSq41C1b/l8gI9PMH+NH222I4uIef+mgoAs5IyOnHPNAJyOCT296qyahaxo2ZlYjjajbifQcVzOqeJy5kSNWijUZ5BAI+vf8P1oDyOiu9YtLTCyPuYtg4IwD6ZP8qzdc8UWWmpCiXCh51LAlSSvPTH19a8+PiSV5XlSJJF2lQJCeQeMgdqsW9/BqFuIL2LeoOQT95fcGqStqxeRdnuZ7uctJOJA5yQBtA+uetU76edUKlWULgghePQ/Wp1G2MyrIJIh0cDBz6EdjWfLdymURRq7qXDM+CSfpQ9WTO1iezMbOzGZgzHDEpg/UGtGz1G7028MiXHlxr3kyMj/PY1jWsUhvDAmOBuAcEVqwWl1dKEdEKnqz/Mq/jnk/SnezIiz0LTNRXUNPS8+VVOfmByrY7j2qK51FiSsH4sf88Vhvfw6daW9mA4SMBVSNDx/tHsKqy3b3C4+5HnhQev1qW7G8Ytlye+C5CfvHz949Af61SVvMkDzkvxjHSmr8uGG3joO1SEhjnaBj8KzbNlFIaqx7m2jGPu56j8aiwTuIYls85qcNjIYgjHBx0NMOwhjnHHHOaVykVwGDFlba35U66gttTURXi7ZgMLMo+Yf4ipFXOcdSO5602VF+XgZx1B6U7tbEygpLUwzorWV0z3XzRLzG6chx/iKuNPE8KFPkLgMRuyP/rf/XrRiuDEPLfEkXo1UzY2z+ebWXzdmGEZGXj/AMRzVN861OSpScSrLM52RLFubP3QMknFQtbzCFiQEIIGxmwT9BUAuBHNkEbg/B6AVek1AyBTIRIoxkAcZ9c1Gq2MbFZI5YQA3ybgTn68ZqRLxogUcqFKksOvI9Pek1HUxcLtYE8Aggcqe4+lLZWenTFZpZ55vVETA+hNaJX3KUS/bme+YFEbYSCXY5ArXjSKNdoWNsdS+c1At7ZxRhI4JlUDACjH9KkGoQqAFsJWAHU5yaaijVQS3MAWyvIxilRIjj7zE8Y6jjNWIEl8vyoY1cDJWR8jPt/kVXhmjlnMsahW/iDKSGz9asafcB5kT+NQd2Oc8+9cjT6mNmY9zY3c8t1cyHdIku1hjrgc/TApkaXsM6ZGQyEgHB+UV2jac7wvDHny5G/eHGMZHUetPXwraNKkrzSsyjghtuPpVxrq1mXy3RzUen381uzRQsqkMVBlC4P0J4rHktJlfbMfLwTkEgDGOtd9q+nWdrp5eR53C4AzLj8+K8/vpBdXB2fcA+UZOMdepq6c2yWrMdM2bUzLL5jqQpzyPYiobeJJvlknEYJ7+veqkhCAAdMDn1qNWO8ehrRLQFobMlpsCP5wfdwOcHFAjxnls1Grts8oHKA5HHNWIUOd2RsHXPpSW2pvHRXYbBgEk/jUUShrkAnpk1dnPkxjDqUPfFU4ZN92o27uvIABoTvqVdE00PlxMyksVXPSq0TzuXBC/KpP3Mc4rSmjdbchYwTgjaD19/aqMckfmSxgEkqwJ3kgnvTikyKj10FYsluXSXy5QcEICDjNWtU3Np7FnZjwOfrWTHepM+3y8Enru681q6p/x5sMEEsAOeKGrMqnrFs56ZWgmaLg7eCSvWrem+Y9zGcjG7aRjrkH/Cqt4Cl3IrEFgxBIOc1Y0ueMTJEepkB6dgDWj1EraGnf391bGMpPIq52lVwc8d81Un1e42NASQ4Iw2cFcVLqUTzKhRflRtxJ6YpsdhcX5a4mUeXGNxzxwSOPXvUXja7M6jVyB5pgEuEdy6KNzE5B78d8c0ui31yl6EEzhXwMBiMc9vSugsbG1it5YbpVeBQolaI7ZAOvynvwTkcZx1FUoBpsfn37xOqJLthRW2gD1OMn04HvSjUUtETA3nuLj7MVMjtlcZPf3q1a2bywIx6kcj0qqrCRFkiY7WxhSc10GloDaIW5PPX61G7sztekboof2a3qelO/s5toHPBreEa46U4Rr6CjlJ52YH2F8EHPP0qP+z23Zyf0rpPLT0FNMS+gp8o+dnOtZvnP6dqZ9kkXkD9K6MxJ6VE8S4PFLlFzs5W5iMUL7wAB82ccio9Nls4Ly3a8hJhVgZJIkBk299tauqxgR4AznFYc6/KxGPunmnew7cy1NaT/AIQm78QTG6/tCKx8oNHKq/vDJ3DKAR+NUPEdt4cSOIeH7+4lzkSC6Qrj0I4+o/CsRhiQN/EOAaeXAiAz8+/P4Ypc4nRiV0tY3uIzPMpjziTYcEDHbj6Vb0F47JZjcyKpcqR36f8A66g5Cnnn0oxxtqvasn2KOhfVLVApjAnLMF2htuM9+laYQMMhf1rjVX99GSSuGBrqxKcck5q4O5Mo20KWrWWq6hdrcKrDgK6eYAMDvUdpo1zDM8xgKP8Aw7ZAc/4V6RL4e8skRyNJ6FQoB/Nqrf2JfYP+jKf+2i/41wtztaxi4y7HJv8A2jICDGRt+7kjmtMSDaA2c4rZOhahnItSfo6/4006HqDf8uk34EH+tYuMuwNSfQ57UZDcWUsDiZ0ZT8qjAPpzXnN5p99hVSymjwOcIxzXsjaJqAH/AB5z4+g/xoGkaj3tJf8AvitYVJQ6E8r7Hhz2d8xG+1nG3jiFuf0qWHTr6WZd9tdMp4z5Z4/Svav7OvUBJtbj8Eo+w3mf+Pa4P1Q/4VbxErbBZnD2eg2TW4MkVzvZRjajAg9KrT+G5WGLZbhQDzvjJB/KvQRp96f+XWc4HZKDZ3a8tbzj/gB/wrn5p3uU27WseeRaJcWyASRTzOTnb5BCj/GhdDhLMDa3EWB/rFVuM+gxzXoJt7nOPJmHt5bf4U9YLgdY5s/9c2/wp+1mGp59DZqA4kjvioyoDwn5x+XFRTaPayw+VBavBKAVM21+T+PHAr0jybnB/cz/APfpqQxznrDN6f6s0lUkncLnlR8P2dvJHiW6diQCduB7npxWlcaI92gigulbefl+TJz74r0PypScNFNj/cNPhhCyKwWSNlIKnyzwf6VarTuNSsjxq58Ma4J3LabeMSfvLbvg+44qxpHhy4g1GGfUh9lgBOVl+VyMYztPQc9a9wTxDqMbAGdnH+1D1qO51d7wj7XaW8xHAZomBH45rZ4m6sU2rbnjF09vDJbeawaCQkusfVVBIHHY/wA6fb3FtbRtCkZmlkDecc/dXqAMdeM16w8tm2f+JfCp64UkfzqvNZaRcoGl0tMf3lkA/pWftlszJxV7nmN9qSLYh7Ys0RO35kzg9QCw+8cEdRT9Fit59MKXUDSgsxC4I9Otd1f2mlxWLJFay4ZshDcnaT+XNc0tn5cT5OSzFuOPpgVtSmraG9KDevQX5AQYkZEJ+XPb2/lXRaW+20TJrLhUJ5MdxGZ7Zm5iVtpGPft16119lY+HSRETqMBHX96HA/IZqlOKeptN2SRUEg9RxTvMFdLb+FNJu03295cyKOuHH9VqX/hCrLtc3f8A30v/AMTWnPFmdmcrvFBkFdT/AMITaEY+13X5p/hTT4ItycC+ufyT/CjmiGpyxcVE7jBrq28DRZ41Ccf8AWoJPAbfw6nL+MKn+tHMgszgdXf5ODjkdTisN9rMckjr/EK9Pn+HBn+9qkh+kC/41mT/AAzvYyRFeLKp6ZQKR+tTJouLtueXyR4nz3z/AFokGGNegy/C7UWk3CYE+2P8aqz/AA01ZTwGYf7KA/1rK6Lc4nDEfNjvinbstz6V1zfD/UYmy6Tg/wDXuTVSXwfdxZzJj/fiZf6UudE+0ic4FJkXk8MDW8bgd80HwzKzqHniVQcnrk/Tir48P2oH/HzP+Dj/AAq414xMp1It6HVBjml3t60UV2EDxIw/iNO8516M350UUrILseLiXtI/5mnfa5/+er/99GiijlVguxwvrjP+uk/76pwvbgH/AFz+xzRRRyrsF2PW+uRx58n/AH1Tv7Ruh/y8Sf8AfVFFChHsO7HDUrzp9pl/76pw1K8H/LxJ/wB9UUU+SPYLscNUvB/y8P8AnSjVb08ee1FFRKEewXY4ape4/wBe1KNUvR1nY/lRRSUUO7EOqXbMpMxJGccDj1p41W86mY/98iiiq5I9hXYp1K56iQde6ChtQucH94v/AHwKKKHCPYLsadRuD1ZOP+mYphvpznPl4J/55L/hRRS5I9h3YLfTdMRen+qX/CnLqMyklRED6iMA/pRRS5I9h3Y4axdj/lqeak/ti96+YPxFFFJxRN2B1u9z99f++aT+3L3+8n/fNFFHKh3Yv9uXo7x/980067eMOCg59KKKOVDTY7+3LwdfLP4Uv9u3npF+VFFPkiDbEOuXhHOz8qP7eu/7sf5UUUckQuw/t66/uoPoKb/b11nkIfqKKKXJHsK7I5NWlf78MDfWMGo/t697K0J9fJFFFP2cewm2f//Z"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the mailbox made of?')=<b><span style='color: green;'>metal</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>metal</span></b></div><hr>

Answer: metal
