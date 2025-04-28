# Discord Nuke Bot README

**Tiếng Việt**: Đây là một bot Discord được thiết kế với các tính năng phá hoại, cho phép người dùng thực hiện các hành động như cấm hàng loạt, đuổi thành viên, tạo vai trò, v.v. **Sử dụng cẩn thận** vì các hành động này có thể gây gián đoạn nghiêm trọng cho server Discord. Hãy đảm bảo bạn có quyền sử dụng bot trong server, vì việc sử dụng trái phép có thể vi phạm Điều khoản Dịch vụ của Discord.

**English**: This is a Discord bot designed with destructive capabilities, allowing users to perform actions such as mass banning, kicking, role creation, and more. **Use with caution** as these actions can cause significant disruption to Discord servers. Ensure you have permission to use this bot in any server, as unauthorized use may violate Discord's Terms of Service.

---

## Table of Contents / Mục lục
- [Features / Tính năng](#features--tính-năng)
- [Requirements / Yêu cầu](#requirements--yêu-cầu)
- [Setup Instructions / Hướng dẫn cài đặt](#setup-instructions--hướng-dẫn-cài-đặt)
- [Usage / Cách sử dụng](#usage--cách-sử-dụng)
- [Commands / Lệnh](#commands--lệnh)
- [Packs/Dependencies / Thư viện yêu cầu](#packsdependencies--thư-viện-yêu-cầu)
- [Disclaimer / Tuyên bố từ chối trách nhiệm](#disclaimer--tuyên-bố-từ-chối-trách-nhiệm)

---

## Features / Tính năng
**Tiếng Việt**:
- **Cấm/Đuổi hàng loạt**: Cấm hoặc đuổi nhiều thành viên khỏi server.
- **Lấy Webhook**: Lấy tất cả webhook trong server.
- **Tạo vai trò hàng loạt**: Tạo nhiều vai trò với màu ngẫu nhiên.
- **Sửa quyền**: Cấp toàn bộ quyền cho vai `@everyone`.
- **Tạo vai Admin**: Tạo vai Admin với toàn bộ quyền và gán cho người dùng và bot.
- **Gửi DM NSFW**: Gửi các embed NSFW hỗn loạn đến tất cả thành viên qua DM.
- **Lệnh Nuke**: Xóa kênh, vai trò và tạo kênh mới với tin nhắn spam.
- **Menu trợ giúp tùy chỉnh**: Menu trợ giúp tương tác với danh mục lệnh miễn phí và cao cấp.
- **Thời gian chờ**: Ngăn chặn lạm dụng với thời gian chờ cho lệnh.
- **Server trong danh sách trắng**: Ngăn bot hoạt động trong các server được chỉ định.

**English**:
- **Mass Ban/Kick**: Ban or kick multiple members from a server.
- **Webhook Retrieval**: Retrieve all webhooks in a server.
- **Role Spam**: Create multiple roles with random colors.
- **Permission Modification**: Grant full permissions to the `@everyone` role.
- **Admin Role Creation**: Create an admin role with full permissions and assign it to the user and bot.
- **NSFW DM Spam**: Send chaotic NSFW embeds to all members via DM.
- **Nuke Command**: Delete channels, roles, and create new channels with spam messages.
- **Custom Help Menu**: Interactive help menu with categories for free and premium commands.
- **Cooldowns**: Prevent abuse with command cooldowns.
- **Whitelisted Servers**: Prevent bot actions in specified servers.

---

## Requirements / Yêu cầu
**Tiếng Việt**:
- **Python**: Phiên bản 3.8 trở lên.
- **Tài khoản Discord Developer**: Để tạo bot và lấy mã token.
- **Server Discord**: Để thử nghiệm và triển khai (với quyền phù hợp).
- **Thư viện**: Các thư viện Python được liệt kê trong phần [Thư viện yêu cầu](#packsdependencies--thư-viện-yêu-cầu).

**English**:
- **Python**: Version 3.8 or higher.
- **Discord Developer Account**: To create a bot and obtain a bot token.
- **Discord Server**: For testing and deployment (with appropriate permissions).
- **Dependencies**: Python libraries listed in the [Packs/Dependencies](#packsdependencies--thư-viện-yêu-cầu) section.

---

## Setup Instructions / Hướng dẫn cài đặt
**Tiếng Việt**:
1. **Tạo bot Discord**:
   - Truy cập [Discord Developer Portal](https://discord.com/developers/applications).
   - Tạo một ứng dụng mới và thêm bot.
   - Sao chép **Bot Token** và dán vào biến `BOT_TOKEN` trong mã.
   - Bật các **Intent** sau trong cài đặt Bot:
     - Server Members Intent
     - Message Content Intent
     - Presence Intent
   - Mời bot vào server của bạn với các quyền cần thiết (ví dụ: Administrator).

2. **Thiết lập kênh Log**:
   - Tạo một kênh Discord để ghi lại hành động của bot.
   - Sao chép ID kênh và dán vào biến `LOG_CHANNEL_ID` trong mã.

3. **Cài đặt thư viện**:
   - Cài đặt các thư viện Python được liệt kê trong phần [Thư viện yêu cầu](#packsdependencies--thư-viện-yêu-cầu).

4. **Cấu hình danh sách trắng**:
   - Thêm ID của các server mà bot không được hoạt động vào danh sách `WHITELIST_SERVER_IDS`.

5. **Chạy bot**:
   - Lưu mã vào file `.py` (ví dụ: `nuke_bot.py`).
   - Chạy script bằng Python: `python nuke_bot.py`.
   - Bot sẽ đăng nhập và hiển thị trạng thái.

**English**:
1. **Create a Discord Bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot.
   - Copy the **Bot Token** and paste it into the `BOT_TOKEN` variable in the code.
   - Enable the following **Intents** in the Bot settings:
     - Server Members Intent
     - Message Content Intent
     - Presence Intent
   - Invite the bot to your server with the necessary permissions (e.g., Administrator).

2. **Set Up the Log Channel**:
   - Create a Discord channel for logging bot actions.
   - Copy the channel ID and paste it into the `LOG_CHANNEL_ID` variable in the code.

3. **Install Dependencies**:
   - Install the required Python libraries listed in the [Packs/Dependencies](#packsdependencies--thư-viện-yêu-cầu) section.

4. **Configure Whitelist**:
   - Add the IDs of servers where the bot should not perform actions to the `WHITELIST_SERVER_IDS` list.

5. **Run the Bot**:
   - Save the code in a `.py` file (e.g., `nuke_bot.py`).
   - Run the script using Python: `python nuke_bot.py`.
   - The bot will log in and display its status.

---

## Usage / Cách sử dụng
**Tiếng Việt**:
1. **Mời bot**:
   - Sử dụng liên kết mời của bot (cung cấp trong lệnh `n!help`) để thêm bot vào server.
   - Đảm bảo bot có các quyền cần thiết (ví dụ: Cấm thành viên, Quản lý vai trò, Quản lý kênh).

2. **Chạy lệnh**:
   - Sử dụng tiền tố `n!` theo sau bởi lệnh (ví dụ: `n!help`).
   - Các lệnh có thời gian chờ để ngăn chặn lạm dụng (ví dụ: 100 giây cho hầu hết các lệnh).

3. **Theo dõi Log**:
   - Các hành động của bot (ví dụ: thực thi nuke, lỗi) được ghi lại trong kênh `LOG_CHANNEL_ID`.

**English**:
1. **Invite the Bot**:
   - Use the bot's invite link (provided in the `n!help` command) to add it to a server.
   - Ensure the bot has the necessary permissions (e.g., Ban Members, Manage Roles, Manage Channels).

2. **Run Commands**:
   - Use the prefix `n!` followed by a command (e.g., `n!help`).
   - Commands have cooldowns to prevent abuse (e.g., 100 seconds for most commands).

3. **Monitor Logs**:
   - Bot actions (e.g., nuke execution, errors) are logged in the specified `LOG_CHANNEL_ID`.

---

## Commands / Lệnh
| Command / Lệnh | Description / Mô tả | Cooldown / Thời gian chờ |
|----------------|---------------------|--------------------------|
| `n!help`       | **VN**: Hiển thị menu trợ giúp tương tác.<br>**EN**: Displays an interactive help menu. | 100s |
| `n!ping`       | **VN**: Kiểm tra độ trễ của bot.<br>**EN**: Checks the bot's latency. | 5s |
| `n!setup`      | **VN**: Thực thi nuke toàn server (xóa kênh, vai trò, v.v.).<br>**EN**: Executes a full server nuke (deletes channels, roles, etc.). | 300s |
| `n!massban`    | **VN**: Cấm tối đa 100 thành viên.<br>**EN**: Bans up to 100 members. | 100s |
| `n!masskick`   | **VN**: Đuổi tối đa 100 thành viên.<br>**EN**: Kicks up to 100 members. | 100s |
| `n!webhooks`   | **VN**: Lấy tất cả webhook trong server.<br>**EN**: Retrieves all webhooks in the server. | 100s |
| `n!perm`       | **VN**: Cấp toàn bộ quyền cho `@everyone`.<br>**EN**: Grants full permissions to `@everyone`. | 100s |
| `n!admin`      | **VN**: Tạo và gán vai Admin.<br>**EN**: Creates and assigns an Admin role. | 100s |
| `n!dmnsfw`     | **VN**: Gửi embed NSFW đến tất cả thành viên qua DM.<br>**EN**: Sends NSFW embeds to all members via DM. | 100s |
| `n!role`       | **VN**: Tạo tối đa 250 vai trò với màu ngẫu nhiên.<br>**EN**: Creates up to 250 roles with random colors. | 100s |

---

## Packs/Dependencies / Thư viện yêu cầu
**Tiếng Việt**:  
Để chạy bot, cài đặt các thư viện Python sau bằng `pip`:

```bash
pip install discord.py aiohttp
