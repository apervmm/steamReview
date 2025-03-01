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

- Next, I checked whether or not each attributes has NULL values, and it turned out that omnly games had 5266 unlablebed names, so I decided to remove them completely from the table
**Result:** Reduced the file to 3.5 GBs


