
# MCmonitor

Bot cơ bản giúp bạn thông báo trạng thái server minecraft liên tục.

# Cách setup
## B1. Tạo Bot trên Discord Developer Portal
- Truy cập: https://discord.com/developers/applications

- Bấm "New Application", đặt tên cho bot (ví dụ: ABC), rồi bấm Create.

- Vào tab "Bot" > bấm "Add Bot" > xác nhận.

- (Tùy chọn) Đặt avatar cho bot để dễ nhận diện.
## B2. Lấy Token Bot
- Vẫn ở tab "Bot" > chọn "Reset Token" > Copy token.
## 🔧 B3. Bật Intents

| Tên Intents             |
|-------------------------|
| PRESENCE INTENT         |
| SERVER MEMBERS INTENT   |
| MESSAGE CONTENT INTENT  |

Vào tab **"Bot"** trong Discord Developer Portal, kéo xuống **Privileged Gateway Intents**, bật cả 3 mục trên, rồi bấm **Save Changes**.
## B4 Mời Bot vào Server
- Vào tab OAuth2 > URL Generator.

 Tick các mục:

 **Scopes:** ``bot, applications.commands``

**Bot Permissions:** ``Send Messages, Embed Links, Read Message History, Use Slash Commands, v.v.``

Copy link được tạo ở dưới để mời bot vào server.
## B5. Setup Bot
Vào ``Main.py`` có 3 line từ line 13 đến line 15
- **serverName:** để trên server của bạn
- **serverIp:** để ip + port server ví dụ: 127.0.0.1:25565
- **botToken:** để token bot mà bạn lấy được ở bước 2
## B6. Run bot
**sử dụng lần lượt:** 
- pip install -r requirements.txt
- python main.py


## License

[MIT](https://opensource.org/licenses/MIT)
