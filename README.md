# 傳送匯率報價給 Teresa 老闆

### 1 複製這個專案到自己的帳號
- 项目地址：[https://github.com/ryk001/Send-FX-to-Teresa](https://github.com/ryk001/Send-FX-to-Teresa.git)
- 點擊右上角 Fork 專案至自己的帳號底下

![run](https://s2.loli.net/2022/12/06/1ta8qHFNBWjQuUb.png)

### 2 添加 LINE 金鑰到 Secrets
(如果不設置 Secrets 的話所有看到程式碼的人都可以傳 LINE 給你 😂)
- 回到專案頁面，依次點擊`Settings`-->`Secrets`-->`New secret`

![run](https://s2.loli.net/2022/12/07/7lvh9u3ayXZkIAm.png)

- 建立一個名為`LINE_NOTIFY_TOKEN`的 secret，裡面填上 LINE Notify 的金鑰
- **secret 必須按照以上格式填寫!!!**

### 5 啟用 Actions

Actions 默認是關閉狀態，在 Fork 之後需要先手動執行一次，成功運行才會被激活。

返回項目主頁面，點擊上方的`Actions`，再點擊右側的`Sending-Current-Stock-Prices-With-Line`，再點擊`Run workflow`

![run](https://s2.loli.net/2022/12/07/jQufzoTSVdcbsn2.png)

運行成功後，就大功告成啦!
