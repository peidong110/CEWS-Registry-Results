# CEWS-Registry-Results

Updated:
## 409,733 entries over 280 seconds for main.py and around 100s for multi_thread_main.py


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

###
Decided not to use multi-thread when parsing html files, instead we write files to csv synchronously.

#### to-do
Order of entries is different.
