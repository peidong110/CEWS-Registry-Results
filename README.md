# CEWS-Registry-Results

Updated:
## 409,733 entries over 280 seconds for main.py and around 100s for multi_thread_main.py


### Reminder
If you already know the maximum page(It's 410 right now), then just assign it to max and do not call [get_max()](https://github.com/peidong110/CEWS-Registry-Results/blob/ff6368af88d64594df88d81c51d7de206a92b505/multi_thread_main.py#L114), calling get_max() will potentially slow down the program. This also applies for [inser_data()](https://github.com/peidong110/CEWS-Registry-Results/blob/ff6368af88d64594df88d81c51d7de206a92b505/multi_thread_main.py#L86) and create_table. They are used to create a database file, if you databsae can import csv file directly, then you can just comment the out.
### Crawled Data
![crawledEntries](https://i.ibb.co/j8xqPff/csvfile.png)
### Data from CRA
![cra](https://i.ibb.co/sJ3c1tB/cra.png)



## Multi-Thread:
I used Producer and Consumer pattern to make this multi-thread web crawler work. Time consumption is signaficantly reduce by around 2/3. Producer produced all the html files, once this producer thread completed its work, then consumer thread will then pick up the files and parse it to data we really want.

### Time:
![multi_thread1](https://i.ibb.co/wRs3gnj/multi-thread1.png)
### Data from CRA
![multi_thread2](https://i.ibb.co/W2cPhqS/multi-thread2.png)
### Database Screenshot
![db](https://i.ibb.co/6sY4B07/count.png)

###
Decided not to use multi-thread when parsing html files, instead we write files to csv synchronously.

#### to-do
Order of entries is different.
