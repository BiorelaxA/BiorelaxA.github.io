---
title: vf2-gmac-driver
date: 2025-04-28T11:35:41.496Z
extra:
  featured: true
  link: https://github.com/BiorelaxA/vf2-gmac-driver
taxonomies:
  tags:
    - OS
    - Network
---

# vf2-gmac-driver
visionfive2 gmac driver according to rthread gmac driver,这里是visionfive2 星光二代开发板网卡驱动，驱动基于linux,rthread进行开发。

# 如何适配
驱动适配首先需要依据设备树搜索到网卡信息并拿到网卡地址，之后根据os设计适配platform即可。我们在自己的os上已经成功适配了这个驱动https://github.com/li041/RocketOS/并通过了git ,curl测试，您可以参考我们的设计。

# 注意
驱动并没有实现中断设计，我们依然采用的是轮询设计，欢迎任何PR和ISSUE