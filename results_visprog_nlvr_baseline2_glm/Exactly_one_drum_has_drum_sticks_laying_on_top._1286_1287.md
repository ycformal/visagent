Question: Exactly one drum has drum sticks laying on top.

Reference Answer: True

Left image URL: https://upload.wikimedia.org/wikipedia/commons/b/b9/Aasteeldrum.jpg

Right image URL: https://i.pinimg.com/736x/ab/39/e6/ab39e6a2002f5ed850a8a24000f872a7--drum-band-real-steel.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Exactly one drum has drum sticks laying on top.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABBAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDu6pajJKj2QikKbrpFfH8S4OR/KrW45A6k9BWxpdhHLIxnQOUwQMdPetWyIQb1MZlOMkVC61v3rW1vqEenFlWe5heWOLHJVfvH8MiuY1TVLWy1ey01mH2m5BO0H7qgcE/U8D8am9y3CyOy8LKF0qTH/PZv5Cthqx/DLY0t+370/wAhXlnxb+I93Dcv4f0W4MSBR9quI2wzZ/gU9hjqe9Q9xLY9A1vx14d0W4a1uL9Zbsdbe2HmOPrjhfxIrmbn4lNKpax0OWRDkK09wqbj9AD/ADrx/wAN2g1Cxu44djXKEO8bdWX+8vrgnkVPEZ0gFg8rp5c5ITOAueuD+FTcqx2N/wDFzULSQLP4egUN0/0puf8Ax2m23xd06dwt7pV1Bnq0TrIPy4NcX4kFuBYwwyBzGjCQhtw5PGPyqvo1jG6zTyRF9g+QjoCT15p3Cx7BY65pOtj/AEC8jkfGTE2Vcf8AATzSz2+c8V5vpGgNq9xNdJM0Udv83mjIO89ACO/euv0TXJvtn9k6pIHmHyxXB4L/AOy3v796aZNizJaZfpRWs8I3dKKYG1a/Z3JRZ4/M43IWAI/Ct4azovh+1M+papZ2528mSZcn6Dqa8t8XeGzr9tHJbFEvIuAWOAy+hNedz+CddhmiR7WMGWQRI3nLgsQT1/A1ViufSx2/jb4qWs3iaHUfDa+c1vaSWomuIyFBdgSyr34HfFcx4Qi1HX/FA1K4mllMUnnXFw5ySey/U+nYU/SvAijXTY6tPuC24uCtu3XLbdpJH8q9ItLa20+1S2s4EhhToiDA/wDrn3ppImUtDrtHWeXTo1hcCP7SfOHAJXHQfjivmvxfbTWnjHVkuMiQXTvz1IJyD+VfS3htv+Ja/wD11P8AIV5z8VPDMWpag13ENl0FGGH8Qx0NRJXYR2PGbedoZfOhZo3x1U1ca9mu5MzSFmH+c1Xlt5rWTy5oyrL7dafCinpnd2xUFF+0tMwzXUq5jQqqjpudjgfkMn8K7PQvD66zqn2C0i/chSXfJwK49dS8lrSEwyiC3fzGAA/euen4AV2+neKTLKYUf7LauBlv9Xg+pCHcw9silqUdZNptn4ZszE0sfkxDJRDlmc9Rj1P6VwuvXMk0hvjGkHQRKg6HqB9ferup3+l2SOmnq9wztvkuZFCGRug47ADpWNp8j6xrsCTsJIIT5hjXhRjt+dNJslnp4bcil+GKgke+OaKxtMuma02PJIxjdkDynLMM8E0VZJoXF3DaQPNPKscaDJZq53U76S5a1mkufsym4VIoEkXeoIPzt1+b0HQd8k1e1OxtJY5Z3t0aQ4yzDPpVeSztQ4WK3iTjqqAc1QLQzLXWoYvE1y95eQyEWiRrNCCVbDEnIGdp5HFdPDdJNEkkZyjjIOCOPxrkbbA1W+mUANGkOcf8C3V0Uc24AjvTSJkd94ZfOmN/11P8hWR40jJeKUj5WXbn3FaPhVs6S/8A11P8hV/UrKLULR4JhlW7jqD6ipvaQ+h4tfWEM5YPGGFYU+gxxtvhcqfQ9K7vW9CvNNdmMbSwdpUGfzHauamfOQDWnKpEXaOektmVhvVWA7A//Wo+0eSPlhGR056VenJJPWs2fk4701SiS6kivcXk9w2GYKP9kc/nXaeB9PIt57krwcID+p/pWNovg/UtXnVzA9va5+aaVccf7I6mvUbXTobCzjtbddscYwM9T7n3pzcUrIKak9WZ7QnNFX2i56UViambfSZtJV7lTWcbqOK1E8rhECgliabe3cytsjtXmDLyQwAH51hJb6m8qvMkLBP9UjOSE98Y5PvTAdbalHFqWoTSwTRwSunzsvC/L/EOoznNbWmSmSHbvDbDgEHOR2NZUVlfCaeY3ESmVtzAJnHAHc+1S2ejtGzsLuaMOclY8KPyxxTQm0dda/ELw74Wi+wavdyxXDHzQqQM42ngHI+hqY/GXwQf+Yjcf+Aj14h8SF2eIbdMsdtogyxyTy1cfUPcpbH0y/xg8EN/zELj/wABHrLuviJ8O7okyyFye5sWz/Kvnqii4WPdj4x+GROdmT72klWIPiF8PrQ5tmER9VsWB/PFeA0UczDlR9Dt8VfB5/5f5/8AwFeom+KPhA9L6f8A8Bnr59oouFj30/E7wkT/AMf03/gM9FeBUUh2PoHvUI/1hooqyBp/1f41ZSiimtyWeXfEr/kZYf8Ar1T+bVx1FFQ9zRbBRRRSGFFFFABRRRQAUUUUAf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Exactly one drum has drum sticks laying on top.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

