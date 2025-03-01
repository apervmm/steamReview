# Cleaning Parts & Difficulties

- Initially, while I was converting `csv` into `parquet`, there was one mismatch in the datatype in one of the entries, so I removed the whole chucnk of dataset where this entry was. Since there are already enogh entries, I decided to run with fewer amount 

**Result:** Reduced # entries by 500000 :D

- Also, I wanted to clean/remove attributes such `hidden_in_steam_china`, `steam_china_location`, `timestamp_updated` and create new `games` table with associated `appid`. However, I have runned to multiple issues, where unique number of games were different in both tables and did not corresponded, so I decided to keep `game` attribute and remove `appid`. 

**Result:** Reduced the file to 22.35 GBs

- Then, I removed `review` column because of three reasons:
    1. Difficult to evaluate categorical string data
    2. Many different languages to parse
    3. Takes a lot of memory

**Result:** Reduced the file to 3.61 GBs

- Next, I checked whether or not each attributes has NULL values, and it turned out that 5266 columns of `game` attribute had unlablebed names, so I decided to remove them completely from the table

**Result:** Reduced the file to 3.5 GBs


# Confidence Gaining
- Confidence on **Hypothesis 1:** Reviews from users who have purchased the game (as opposed to obtained it for free) will be rated as more helpful


<img width="285" alt="image" src="https://github.com/user-attachments/assets/565fb4d9-902f-4179-a6ab-da5f46682c3e" />


- As it can be seen there's already a significant difference on average `helpfullness` to prove that purchased game will likely be more helpgul

  
<img width="402" alt="image" src="https://github.com/user-attachments/assets/32db8605-e640-4ad4-8c3a-a3f92b5b3584" />




- Confidence on **Hypothesis 2:** Reviews written during a game’s early access are more likely to be critical about the game specifications and expectations.

  
<img width="349" alt="image" src="https://github.com/user-attachments/assets/e4cebed1-1bbb-4c53-962d-a703dc24ecdb" />


- As it can be seen there's already a significant difference on average `helpfullness` to prove that early stage reviews will likely be more helpgul


<img width="519" alt="image" src="https://github.com/user-attachments/assets/56457a1e-8be8-4ab7-a09c-01810afe9019" />




