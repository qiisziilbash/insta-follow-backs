# %%
import re

# %%
with open("data/following.html") as file:
    following_text = file.read()

with open("data/followers_1.html") as file:
    followers_text = file.read()

# %%
pattern = r'href="(https://www.instagram.com/[^"]*)"'
followers = set(re.findall(pattern, followers_text))
following = set(re.findall(pattern, following_text))

# %%
print("These Shampalets are not following you :)")
for item in following - followers:
    print(item)

# %%
print("These Pompalets are not followed by you :)")
for item in followers - following:
    print(item)
