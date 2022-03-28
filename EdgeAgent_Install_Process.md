<center><h1>智能终端安装手册</h1></center>
[TOC]
<div STYLE="page-break-after: always;"></div>
## 1 BIOS设置
### 1.1 复位BIOS设置
示例
F9 = Optimized Configuration
![Optimized Configuration](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\OptimizedConfiguration.marked.jpg)
### 1.2 允许网络启动
- 允许局域网PXE启动
	示例
	Advanced > Lan PXE Config > PXE BOOT = Legacy
	![PowerFailure.finished](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\OverAll.Network.jpg)
	![PXE](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\PXE.jpg)
- 配置网络协议堆栈
	示例
	Advanced > Network Stack Configuration > Network Stack = Enabled
	Advanced > Network Stack Configuration > Ipv4 PXE Support = Enabled
	![OverAll.Network.jpg](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\OverAll.Network.jpg)
	![NetworkStack](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\NetworkStack.finished.jpg)
### 1.3 打开来电自启
示例
Advanced > SIO MISC Configuration > Power Failure = Always On
![OverAll..jpg](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\OverAll.Power.jpg)
![PowerFailure.finished](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\PowerFailure.finished.jpg)
### 1.4 保存并重启
示例
F10 = Save & Exit
![SaveChanges](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\SaveChanges.jpg)
## 2 操作系统安装
### 2.1 **临时**从网络启动
示例
DEL进入BIOS
确认1#网口位置
Save & Exit > BOOT Override > Realtek PXE B01 D00 = 选中
NOTE: 某些工控机标注网口和实际网口相反
![BootOverride](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\BootOverride.jpg)
### 2.2 网络安装Ubuntu操作系统
Install Ubuntu (mannual）
NOTE: 耐心等待安装结束（时间较长），无需公网连接
![InstallUbuntu](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\BIOS\InstallUbuntu.jpg)
## 3 终端软件安装
### 3.1 修改配置文件(config.xls)
- 风场信息sheet页
风场名 = <风场名称>
NTP时钟源 = <SCADA服务器IP地址>
	示例
![点表样例_风场](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\点表样例_风场.jpg)
- 风机信息sheet页
	风机 = <WEB界面风机名称>
	环路 = <风机所在环路名称>
	生产商 = 上海电气
	风机点表 = <风机对应主控点表> (隐藏sheet页中必须存在“测点表#上海电气#<点表名称>”)
	主控版本 = {4.2|4.3|4.7} (AS版本)
	主控地址 = <主控IP地址>
	终端名称 = <终端后台Linux主机名称>
	终端地址 = <终端后台Linux主机IP>
	终端点表 = <终端监控点表名称> (单硬盘 = 终端监控_工控机A | 双硬盘 = 终端监控_工控机AB)
	- 开发板
	  终端监控_树莓派AB
	- 工控机 (A表示单硬盘； | AB表示双硬盘；)
	  终端监控_工控机A
	  终端监控_工控机AB

	冗余组 = <空>
	忽略标志 = { <空> = 有效记录 | 1 = 无效记录 }
	备注 = <根据需要自由填写>
	NOTE: 所有单元不能包含半角逗号(,)和半角引号(")
	示例
	![点表样例_风机.jpg](F:\Internships\Internship_ShanghaiElectric\工控机健康点表完善\工控机程序安装流程\点表样例_风机.jpg)
### 3.2 上传配置文件(config.xls)
- 本地电脑
[安装FileZilla](https://www.filezilla.cn/download/client)
- 上传文件
本地登录智能终端 (缺省用户: sec  | 缺省密码: 123456)
查询智能终端IP地址: ip addr
从Windows笔记本上传配置文件(config.xls)至智能终端/home/sec目录 (缺省root密码: znzd@sewp)
### 3.3 初始化智能终端
```shell
su - (缺省root密码: znzd@sewp)
mv /home/sec/config.xls /root/
cp /root/config.xls /tmp/
单硬盘执行命令: ./installer INIT /tmp/config.xls xxx
双硬盘执行命令: ./installer INIT /tmp/config.xls /dev/sdb1
```
### 3.4 重启智能终端
```shell
reboot
```
### 3.5 启动后台服务
登录智能终端 (用户: agent | 密码: znzd@sewp)
- 配置通信协议
```shell
enter_prod_mode.sh tcp
```
- 启动EdgeAgent服务
```shell
sudo systemctl restart EdgeAgent
```
- 上传主控点表
```shell
upload_point_table.sh <主控FTP用户> <主控FTP密码>
```
通知重启PLC
- 测试端口连通性
```shell
nc <主控IP地址> 3000 | hd -v (数据不断滚动刷新即为正常)
```
