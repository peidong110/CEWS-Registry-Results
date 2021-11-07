# CEWS-Registry-Results

Updated:
## 409,604 entries over 312.3491418361664 seconds


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

### to-do
Some potential entries are lost (~5000)
Something probably went wrong with my multi-thread design.
:upside_down_face:
