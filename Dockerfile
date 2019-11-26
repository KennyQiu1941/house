FROM 4a4618db62b9
RUN yum update -y
RUN yum install -y openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel
RUN yum install -y python3
RUN yum install -y python3-pip
RUN python3 -m pip install -i http://mirrors.aliyun.com/pypi/simple/ --upgrade pip
Run pip3 install -i https://mirrors.aliyun.com/pypi/simple pymongo redis pymysql zmail scrapy lxml requests DBUtils selenium scrapy-redis scrapy-redis-bloomfilter
#添加用户名密码是容器可以ssh连接
RUN echo "root:xxxxxxxx" |chpasswd
#安装screen可以在断开shell时候继续运行
RUN yum install -y screen
#添加中文
RUN yum install kde-l10n-Chinese -y
RUN yum install glibc-common -y
RUN localedef -c -f UTF-8 -i zh_CN zh_CN.utf8
RUN export LANG=zh_CN.UTF-8
RUN echo "export LANG=zh_CN.UTF-8" >> /etc/locale.conf
ENV LANG zh_CN.UTF-8
ENV LC_ALL zh_CN.UTF-8
