# CNS - Homework 2
https://hackmd.io/I7JQw4xTS2-YrYc9XI81lg?view


## 1. My First Project

李鈺說可能可以用 guest lecture 那天有提到的 tool 測測看？
-> 396: int index 改用unsigned int

pm 的project name應該可以做format string exploit

## 2. Pok ́emon Master 

`hint from TA` : This challenge is not related to any web exploitation, and this challenge is running in multi-thread

關鍵在如何把所有的寶可夢名字寫進那個 file ， 因為他 server 寫寶可夢的 file 是用 `'a'` ( append 的方式 ) 加上他 server 有開多個 workers 跑，所以可以用 multi-thread 來處理


一開始先用 `r = requests.get("http://140.112.31.97:10161")` 

然後在 `r.url` 會得到 `http://140.112.31.97:10161/[uuid]`

接這用 multi-thread 去 

`requests.get("http://140.112.31.97:10161/[uuid]/buy?name=[寶可夢名字]")` 買那三隻寶可夢


最後在 `requests.get("http://140.112.31.97:10161/[uuid]").text`  就可拿到 flag 了 


## 3. Fuzz it! 

`hint from TA` : 
You can use Radamsa as a tool to randomly mutate an input, then you need to receive the coverage information and save the seed if you get new coverage.
Note that you don’t need to receive 5 flags in one connection, you can keep fuzzing until you get 5 flags.


## 4. Symbolic Execution

> [Docker and KLEE](https://hackmd.io/@cXpZn6ltSku4Vwx_OL0bqA/r1RGUec0G?type=view&fbclid=IwAR2pcrIpmPQvmmKiA993s4p9w0n3n_fORBlUMTTJIrQKXbMerU_llipcvYA)

`flag:BALSN{P4tH_3xpl0s!oN_b0oo0oO0o0oOO0ooOM}`

照上面的載完後，由secret可以發現第一個是80，下一個80分別是index第25或31，可以知道只可能有25或31個不是"-"的input char，又由index大小可以直接猜除了8,13,18,23外其實都不是"-"（31*32=992），也可以知道在check1中只需要算第一個index與其他的xor即可（後面的不可能改變），照此改code就可以了。

## 5. BGP and Network Model 

> [BRITE - Boston university Representative Internet Topology gEnerator](http://www.cs.bu.edu/brite/)

> [NetworkX](https://networkx.github.io/documentation/latest/index.html#)

用 VM 建立環境 ( 我用 `ubuntu 14.04.6` )

> [OSBOXES - Ubuntu](https://www.osboxes.org/ubuntu/)

去載 [BRITE](http://www.cs.bu.edu/brite/download.html)
( 後來發現好像也可以直接 clone 那個 github 下來 build )


照題目給的 [github](https://github.com/nsol-nmsu/brite-patch) 的 installing 指示做完，就可以弄出 GUI 介面


參考 [BRITE User Manual](http://www.cs.bu.edu/brite/user_manual/BritePaper.html)，我是批次產 config 用 command line 去跑產生所有的 `[AS NUMBER]-[m]-[id].brite`


### 1.



### 2.

BA 是 scale-free graph
Waxman 是 random graph

> [Wiki - Random graph](https://en.wikipedia.org/wiki/Random_graph)

<iframe width="560" height="315" src="https://www.youtube.com/embed/yisN77RMAAA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

> [Wiki - Scale-free network](https://en.wikipedia.org/wiki/Scale-free_network)

<iframe width="560" height="315" src="https://www.youtube.com/embed/qmCrtuS9vtU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

因為 real world network 通常會需要有 pow-law degree distribution ， 所以選擇 BA

如果要了解得更詳細可以去看下面這本電子書

> Guanrong, C. H. E. N., Xiaofan Wang, and Dinghua Shi. "Complex Systems and Networks: Dynamics, Controls and Applciations." (2016).

### 3.


去 parse `[AS NUMBER]-[m]-[id].brite` 裡面的 node 數量和 edge 數量

他說跑個情境跑三次取平均，但是我同一個情境三次的 node 數量和 edge 數量都一樣...

### 4.

找 `AS2` 到 `AS100` 之間的 shortest path 上的 `ASes` ，然後計算這些 `ASes` 的鄰居數量的加總 ( 我不確定我有沒有理解錯 )


去 parse `[AS NUMBER]-[m]-[id].brite` 裡面的 edges

用 [`NetworkX`](https://networkx.github.io/documentation/latest/tutorial.html) 建 graph 找 shortest path 然後找 neighbor

## 6. SSL Stripping 


用 VM 建立環境 ( 我用 `Kali Linux 2019.1` )

> [OSBOXES - Kali Linux](https://www.osboxes.org/kali-linux/)

VM 開起來前記得去設定 network adpater => 設定成 `bridged` ( 預設是 `NAT` )

`ifconfig` 可以看這台 VM 的 interface 和 ip 

`route -n`  可以看 default gateway


### 1

[Arpspoof工具](https://wizardforcel.gitbooks.io/daxueba-kali-linux-tutorial/content/58.html) 的 9.8.1 照做應該就行了


<iframe width="560" height="315" src="https://www.youtube.com/embed/ASgbchlOkJE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 2

<iframe width="560" height="315" src="https://www.youtube.com/embed/b3ZdP0TnsXo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

這個影片的順序比較容易成功的樣子


我們只要做到 `sslstrip` 那個步驟就行了



victim VM 用新的無痕視窗用 http 去連 myntu 


![](https://i.imgur.com/TwOsxjs.jpg)

然後點左上解的那個登入，之後輸密碼然後 `tail -f sslstrip.log` 那個視窗就會噴出東西，理論上要看到

`user=test&pass=test123&Submit=....`

要看到這個才算成功

沒成功的話多試幾次應該就會成功了
