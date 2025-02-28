Question: What is on the water?

Reference Answer: boat

Image path: ./sampled_GQA/210804.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What is on the water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What is on the water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEMDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD1ny2644pQcH0qXJHpTSm89KVxibvelChqd5RHRaX7qknjFMQbQKeB71j+G7xtS0ZLiX7+9lPPoeK20AxxQwQA4p2c9qdt9qQ1JQ3A9KKXNFICmBk1KooVakCUXCwgB9ar6gwg026mLYCQu35KathayvE7+X4Y1Fh1MJX8yB/WmmKxgfD2RpdKuoWP+qnGB7FR/UGu2RcVwHw5k23WpwHusbj8yK9BWqnuKOw6mGnGmMazLG0UmfaigBiVKKqJJ71KHqLjJ81geNX2eFroD+No1/8AHh/hVvV9bt9FtFuLgSMrNtCoMnNcRr/i6HXdGa2S3eFxOGwzZyozzn+lXG7ZMtEJ8P5tviS4i/56WzfoymvSZ7mG0haa4lSKJerucAV5V4Hcr4tgKrndHIpwPVf/AK1X/HuuXa6ydMiaSOFbdJW2uwBO4nOB36DPtV1PiFDY1/EPjy3sZFj054rlVBM7hgQAQcBTnls1maJ8UrWVVh1iD7KUi+a4Ql1dhgfdAyM9eteZ6kbiTzHiKCFPLZ9w5Yn0yMn3p1pBavbg3Wwuc5VnPT6D/Gp0sPU9qHjnw0wz/a0I+qsP6UV4q0VhnhbZR1x5JOPzopWRRsWnjLXRdRGbVJ/L3rvyF5XPPb0r0qLxv4emlCR6nGxOTwrYUD1OOK8KuVvwhnuLOZVjGSxXAFETXwJeGCfDD7yZwRQ4piTPVvFvifR9S0qOG2vo3kEqtg5XAwc5yOO1cGb2PJCyIevQ8k+lc7LdbV3MCoyeC2SD+NEM6KVPyEZyQ8mOfypq6VkGjZ00OvXdggu4btomjXAVDgnjpx061VOuS6mjXVy7NIUKfMS2ACPX8awri8VpARAVB6Ksgbj60xJfLZlYSZYNjK8evJoSBs0ZbjGhEFxkDhd3+16Z/pThOx5LHbnOB35rFuZN0DorqML0BHPsPWtJHTyVPnIV4HQ9ScDtRYLjZJW8w/vX/WikWykuB5sZjKN0OP8A7GilYD0+Wzs7qAwzrK0bjBVpDg0xNIt7e2WABhGpO1YnZQBnOMGr4toEupZ1eZw4AWNiAEx3GOTmrQ2sOxrO5Zw+leFJLTVJbmZop4mBCoy5xzkda07/AEFJo2xFAp7b4PMA/HrWhq2uQ6ZcpbDYszLvO8Hge3FZV74ikmixFJIjxqGxAw3OcjjBx0/xqkmxXSOcl8Mwu2ZIYS3/AExcJ/QVXPh7Z/qp7tG7Dzc8/hW4PEM5QGSO+BUE/vLeNy3tnPWmT6rbtMolids4G4WeQMnHY/5FPlkF4nNnS7kuYxqtsjDoZ2AOT+FFvYanazEqmm3pC5DJOgJP5j+VaraNo16+be51ESlSzGRNqqQe24GqsvhJgQ1reliepeEYJ+qmi9txWvsGzUe/h6XPfZNHj8OaKrN4Z1MMf9Mtj7kuP0op8yDlZ6oGqVGUHJUE+9UxJ9KkEuPSsix15a294waWNGYcZK5rHuvD1ox3pEgY9cRr/wDWrZ8wdeajkk4J60Ac4fDcLjZ5bAA5zjGD+dRSeGUjPHmlT1/eNx+Zro1l55/lSySrjOTg98ZouBy8nh22CZd7kg8YElalogtLeOCJv3Sj5Q6gn6HHNWJSrD7zkewpi85VWcj0AouOw8iZjnPWik+qn8aKAJ1JyafnBxRRQIfk0yToDRRQBErc54zT2YkZoooGV2YlgOOfagxZYL5j4PvRRSAX7Mnq/wD30aKKKAP/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is on the water?')=<b><span style='color: green;'>boat</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>boat</span></b></div><hr>

Answer: a large white boat with people on it

