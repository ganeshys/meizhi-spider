# meizhi-spider
爬取妹子图。。就是爬!

# 在一个寂寞的夜晚，，顾叔叔偷偷爬了爬妹子图，，其中有个地方超级坑，，，是盗链。。


爬妹子图的时候要特别注意盗链，，不然她会给你返回403，，，你就什么都看不到咯

因为一些网站在解决盗链问题时是根据Referer的值来判断的，所以在请求头上添加Referer属性就好（可以填爬取网站的地址）。

另外Referer携带的数据 是用来告诉服务器当前请求是从哪个页面请求过来的。


就爬了一点时间就停了，，结果也上传了。。。可能整站爬有点慢。。。以后有时间再加多线程、多协程之类的。。
