<center><h1>�����ն˰�װ�ֲ�</h1></center>
[TOC]
<div STYLE="page-break-after: always;"></div>
## 1 BIOS����
### 1.1 ��λBIOS����
ʾ��
F9 = Optimized Configuration
![Optimized Configuration](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\OptimizedConfiguration.marked.jpg)
### 1.2 ������������
- ���������PXE����
	ʾ��
	Advanced > Lan PXE Config > PXE BOOT = Legacy
	![PowerFailure.finished](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\OverAll.Network.jpg)
	![PXE](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\PXE.jpg)
- ��������Э���ջ
	ʾ��
	Advanced > Network Stack Configuration > Network Stack = Enabled
	Advanced > Network Stack Configuration > Ipv4 PXE Support = Enabled
	![OverAll.Network.jpg](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\OverAll.Network.jpg)
	![NetworkStack](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\NetworkStack.finished.jpg)
### 1.3 ����������
ʾ��
Advanced > SIO MISC Configuration > Power Failure = Always On
![OverAll..jpg](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\OverAll.Power.jpg)
![PowerFailure.finished](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\PowerFailure.finished.jpg)
### 1.4 ���沢����
ʾ��
F10 = Save & Exit
![SaveChanges](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\SaveChanges.jpg)
## 2 ����ϵͳ��װ
### 2.1 **��ʱ**����������
ʾ��
DEL����BIOS
ȷ��1#����λ��
Save & Exit > BOOT Override > Realtek PXE B01 D00 = ѡ��
NOTE: ĳЩ���ػ���ע���ں�ʵ�������෴
![BootOverride](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\BootOverride.jpg)
### 2.2 ���簲װUbuntu����ϵͳ
Install Ubuntu (mannual��
NOTE: ���ĵȴ���װ������ʱ��ϳ��������蹫������
![InstallUbuntu](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\BIOS\InstallUbuntu.jpg)
## 3 �ն������װ
### 3.1 �޸������ļ�(config.xls)
- �糡��Ϣsheetҳ
�糡�� = <�糡����>
NTPʱ��Դ = <SCADA������IP��ַ>
	ʾ��
![�������_�糡](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\�������_�糡.jpg)
- �����Ϣsheetҳ
	��� = <WEB����������>
	��· = <������ڻ�·����>
	������ = �Ϻ�����
	������ = <�����Ӧ���ص��> (����sheetҳ�б�����ڡ�����#�Ϻ�����#<�������>��)
	���ذ汾 = {4.2|4.3|4.7} (AS�汾)
	���ص�ַ = <����IP��ַ>
	�ն����� = <�ն˺�̨Linux��������>
	�ն˵�ַ = <�ն˺�̨Linux����IP>
	�ն˵�� = <�ն˼�ص������> (��Ӳ�� = �ն˼��_���ػ�A | ˫Ӳ�� = �ն˼��_���ػ�AB)
	- ������
	  �ն˼��_��ݮ��AB
	- ���ػ� (A��ʾ��Ӳ�̣� | AB��ʾ˫Ӳ�̣�)
	  �ն˼��_���ػ�A
	  �ն˼��_���ػ�AB

	������ = <��>
	���Ա�־ = { <��> = ��Ч��¼ | 1 = ��Ч��¼ }
	��ע = <������Ҫ������д>
	NOTE: ���е�Ԫ���ܰ�����Ƕ���(,)�Ͱ������(")
	ʾ��
	![�������_���.jpg](F:\Internships\Internship_ShanghaiElectric\���ػ������������\���ػ�����װ����\�������_���.jpg)
### 3.2 �ϴ������ļ�(config.xls)
- ���ص���
[��װFileZilla](https://www.filezilla.cn/download/client)
- �ϴ��ļ�
���ص�¼�����ն� (ȱʡ�û�: sec  | ȱʡ����: 123456)
��ѯ�����ն�IP��ַ: ip addr
��Windows�ʼǱ��ϴ������ļ�(config.xls)�������ն�/home/secĿ¼ (ȱʡroot����: znzd@sewp)
### 3.3 ��ʼ�������ն�
```shell
su - (ȱʡroot����: znzd@sewp)
mv /home/sec/config.xls /root/
cp /root/config.xls /tmp/
��Ӳ��ִ������: ./installer INIT /tmp/config.xls xxx
˫Ӳ��ִ������: ./installer INIT /tmp/config.xls /dev/sdb1
```
### 3.4 ���������ն�
```shell
reboot
```
### 3.5 ������̨����
��¼�����ն� (�û�: agent | ����: znzd@sewp)
- ����ͨ��Э��
```shell
enter_prod_mode.sh tcp
```
- ����EdgeAgent����
```shell
sudo systemctl restart EdgeAgent
```
- �ϴ����ص��
```shell
upload_point_table.sh <����FTP�û�> <����FTP����>
```
֪ͨ����PLC
- ���Զ˿���ͨ��
```shell
nc <����IP��ַ> 3000 | hd -v (���ݲ��Ϲ���ˢ�¼�Ϊ����)
```
