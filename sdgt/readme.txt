1、关于
	Sdgt(social dictionary generate tool)通过收集到的敏感信息，结合国人密码心理学，实现了一个简单的密码生成工具，可以在暴力破解方面使用。

2、配置信息
	文件采用UTF8编码，template.txt中收集中csdn中top1000密码，可以把template.txt复制进行修改。每行":"前面是密码因子，后面的部分是值并用分号隔开，例如：
		name:zhang san;li si
		qq:10000;10010
		idcard:100121190000111234
		subpw:123qaz;qaz
		nickname:boy;good;sec
		year:2012;2011;2010
		domain:sina;google
	
3、使用
	sdgt.py  C:\zhang.txt C:\zhangdic.txt